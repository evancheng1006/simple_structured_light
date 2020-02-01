load calibration_parameters.mat
img_fn = [ ...
    "test5_projector_full_256_256.png" ...
    "test5_no_projector.png", ...
    "test5_projector_256_256_mod_x_256_lt_128.png", ...
    "test5_projector_256_256_mod_x_128_lt_64.png", ...
    "test5_projector_256_256_mod_x_64_lt_32.png", ...
    "test5_projector_256_256_mod_x_32_lt_16.png", ...
    "test5_projector_256_256_mod_x_16_lt_8.png", ...
    "test5_projector_256_256_mod_x_8_lt_4.png", ...
    "test5_projector_256_256_mod_x_4_lt_2.png", ...
    "test5_projector_256_256_mod_x_2_lt_1.png", ...
    "test5_projector_256_256_mod_y_256_lt_128.png", ...
    "test5_projector_256_256_mod_y_128_lt_64.png", ...
    "test5_projector_256_256_mod_y_64_lt_32.png", ...
    "test5_projector_256_256_mod_y_32_lt_16.png", ...
    "test5_projector_256_256_mod_y_16_lt_8.png", ...
    "test5_projector_256_256_mod_y_8_lt_4.png", ...
    "test5_projector_256_256_mod_y_4_lt_2.png", ...
    "test5_projector_256_256_mod_y_2_lt_1.png", ...
];

current = im2double(imread(img_fn(1)));
seq = zeros(size(current,1),size(current,2),3,length(img_fn));
seq(:,:,:,1) = current;
for i=2:length(img_fn)
    current = im2double(imread(img_fn(i)));
    seq(:,:,:,i) = current;
end

[w,h,~,N] = size(seq);
new_seq = zeros(w,h,N);
for i=1:N
    new_seq(:,:,i) = rgb2gray(seq(:,:,:,i));
end

% 2 is full dark
decode_delta = zeros(size(new_seq));
for i=1:N
    decode_delta(:,:,i) = (new_seq(:,:,i) - new_seq(:,:,2));
end

% full_dark_delta = decode_delta(:,:,1);

% view distribution to decide threshold...?
%histogram(full_dark_delta(:));
threshold = 0.01; % from synthetic images
known = im2bw(decode_delta(:,:,1), threshold);
%has_data = im2bw(full_dark_delta, threshold);

decode_delta_binary = zeros(size(decode_delta));
for i=3:N
    decode_delta_binary(:,:,i-2) = 1 - im2bw(decode_delta(:,:,i), threshold);
end

% (y=869,x=802) -> bottom right
% inv(camera_intrinsic_matrix) * [802;869;1] = [0.3015;-0.3685;1]
% [3.015;-3.685;0]
% [3.0022;-3.6890;9.9848]



power_of_two = [128,64,32,16,8,4,2,1];

x_code = zeros(w,h,1);
y_code = zeros(w,h,1);
for i=1:8
    x_code = power_of_two(i) * decode_delta_binary(:,:,i) + x_code;
    y_code = power_of_two(i) * decode_delta_binary(:,:,i+8) + y_code;
end

%for i=1:N-2
%imshow(decode_delta_binary(:,:,i));
%pause
%end
%imshow(full_dark_delta(1:h/3,1:w/2))
%imshow(x_code/256)
%pause
%imshow(y_code/256)
%pause


% REFERENCE https://github.com/germain-hug/Structured-Light-Depth-Acquisition/
% Load Intrinsic Matrix
K1 = camera_intrinsic_matrix;
K2 = projector_intrinsic_matrix;

% Compute Rotation/Translation matrices
R1 = camera_extrinsic_matrix(1:3,1:3);
T1 = camera_extrinsic_matrix(1:3,4);
R2 = projector_extrinsic_matrix(1:3,1:3);
T2 = projector_extrinsic_matrix(1:3,4);

d = zeros(w,h,3);
%imshow(known)
for x=1:w
    for y=1:h
        if(known(y,x))
            % Compute A and b
            A = zeros(4,3);
            b = zeros(4,1);
            % Convert points to normalized camera coordinates
            p1 = K1\[x;y;1];
            p2 = K2\[x_code(y,x); y_code(y,x);1];
            % Compute linear constraints -> Camera
            A(1,:) = [R1(3,1)*p1(1)-R1(1,1), R1(3,2)*p1(1)-R1(1,2), R1(3,3)*p1(1)-R1(1,3)];
            A(2,:) = [R1(3,1)*p1(2)-R1(2,1), R1(3,2)*p1(2)-R1(2,2), R1(3,3)*p1(2)-R1(2,3)];
            b(1:2) = [T1(1)-T1(3)*p1(1), T1(2)-T1(3)*p1(2)];
            
            % Compute linear constraints -> Projector (~ camera no.2)
            A(3,:) = [R2(3,1)*p2(1)-R2(1,1), R2(3,2)*p2(1)-R2(1,2), R2(3,3)*p2(1)-R2(1,3)];
            A(4,:) = [R2(3,1)*p2(2)-R2(2,1), R2(3,2)*p2(2)-R2(2,2), R2(3,3)*p2(2)-R2(2,3)];
            b(3:4) = [T2(1)-T2(3)*p2(1), T2(2)-T2(3)*p2(2)];
            
            % Compute the least squares solution
            estimated = A\b;
            
            %d(y,x,:) = camera_extrinsic_matrix(1:3,1:4)*[estimated;1];
            d(y,x,:) = estimated;
            %x
            %y
            %d(y,x,:)
            %pause
        end
    end
end

point_cloud = zeros(nnz(known),3);
i_point = 1;
for x=1:w
    for y=1:h
        if(known(y,x))
            point_cloud(i_point,:) = d(y,x,:);
            i_point = i_point + 1;
        end
    end
end
point_cloud = pointCloud(point_cloud);

pcwrite(point_cloud, 'test5.ply');
pcshow(point_cloud);


