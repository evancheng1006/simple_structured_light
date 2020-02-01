img_fn = ["test5\test5.png","test5\test5-001.png","test5\test5-002.png","test5\test5-003.png","test5\test5-004.png","test5\test5-005.png"];
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

