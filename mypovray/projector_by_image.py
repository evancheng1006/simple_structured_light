def projector_by_image(fov_deg, img, spotlight_size_factor=1.418, projector_name='projector'):
    import math
    import numpy as np
    # assume the extrinsic parameter is unit transformation:
    # matrix:
    # [x    [1, 0, 0, 0] [X
    #  y  = [0, 1, 0, 0]  Y
    #  1]   [0, 0, 1, 0]  Z
    #                     1]
    
    info = ''
    info += '//projector_name: %s\n' % str(projector_name)
    info += '//fov_deg: %s\n' % str(fov_deg)
    info += '//img_shape: %s\n' % str(img.shape)
    info += '//spotlight_size_factor: %f\n' % spotlight_size_factor
    
    
    (fov_deg_w, fov_deg_h) = fov_deg
    (res_w, res_h) = img.shape
    
    
    fov_deg_w = float(fov_deg_w)
    fov_deg_h = float(fov_deg_h)
    res_w = int(res_w)
    res_h = int(res_h)
    spotlight_size_factor = float(spotlight_size_factor)
    
    projected_w = 2 * math.tan(fov_deg_w * math.pi / 360.0)
    projected_h = 2 * math.tan(fov_deg_h * math.pi / 360.0)
    
    min_x = -0.5 * projected_w
    min_y = -0.5 * projected_h
    
    pixel_w = projected_w / res_w
    pixel_h = projected_h / res_h
    
    spotlight_r = 0.5 * (0.5 * pixel_w + 0.5 * pixel_h) * spotlight_size_factor
    spotlight_r_deg = math.atan(spotlight_r) * 180 / math.pi
    
    # print intrinsic_matrix
    intrinsic_matrix = [[res_w/projected_w, 0, (res_w+1)*0.5], [0, res_h/projected_h, (res_h+1)*0.5], [0, 0, 1]]
    import json
    ret = ''
    ret += info
    ret += "//intrinsic_matrix = %s\n" % json.dumps(intrinsic_matrix)
    
    
    # print(min_x, min_y, projected_w, projected_h)
    # print(pixel_w, pixel_h, spotlight_r, spotlight_r_deg)
    
    # example format:
    # light_source {<0,0,10> color White spotlight radius 63.4349 falloff 63.4349 point_at <0,0,0>}
    # print("light_source {%s color %s spotlight radius %f falloff %f point_at %s}" % ('<0,0,1>','White',spotlight_r_deg,spotlight_r_deg,'<0,0,0>') )
    ret += "#declare %s = union {\n" % projector_name
    for ix in range(res_w):
        for iy in range(res_h):
            if img[ix, iy] == 0:
                continue
        
            tmp_x = min_x + (ix + 0.5) * pixel_w
            tmp_y = min_y + (iy + 0.5) * pixel_h
            src_at = "<%f,%f,%f>" % (0, 0, 0)
            color = "<%f,%f,%f>" % (float(img[ix, iy]), float(img[ix, iy]), float(img[ix, iy]))
            point_at = "<%f,%f,%f>" % (tmp_x, tmp_y, 1)
            ret += "light_source {%s color %s spotlight radius %f falloff %f point_at %s}\n" % (src_at,color,spotlight_r_deg,spotlight_r_deg,point_at)
    ret += "}\n"
    return ret


if __name__ == "__main__":
    #arctan(1) * 180 / pi * 2 = 90
    #arctan(1/2) * 180 / pi * 2 = 53.1301024
    #arctan(1/3) * 180 / pi * 2 = 36.8698976
    #arctan(1/4) * 180 / pi * 2 = 28.0724869
    #arctan(1/5) * 180 / pi * 2 = 22.6198649
    #arctan(1/6) * 180 / pi * 2 = 18.9246444
    #arctan(1/7) * 180 / pi * 2 = 16.2602047
    #arctan(1/8) * 180 / pi * 2 = 14.2500327
    #arctan(1/9) * 180 / pi * 2 = 12.6803835
    #arctan(1/10) * 180 / pi * 2 = 11.4211863
    import sys
    import numpy as np
    import time
    
    img_w = 4
    img_h = 4
    img = np.zeros([img_w,img_h])
    for x in range(img_w):
        #if x % 4 < 2:
            for y in range(img_h):
                    img[x, y] = 1

    #print(img.shape)
    #time.sleep(10)
    fov_deg = (11.42, 11.42)
    tmp_projector_name = 'projector_full_very_low_res'
    ret = projector_by_image(fov_deg, img, projector_name = tmp_projector_name)
    #with open(tmp_projector_name + '.inc', 'w') as f:
    #    f.write(ret)
    print(ret)
    