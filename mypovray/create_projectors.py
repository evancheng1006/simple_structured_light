from projector_by_image import projector_by_image


import sys
import numpy as np
import time



#####
tmp_projector_name = 'projector_full_very_low_res'
img_w = 4
img_h = 4
img = np.zeros([img_w,img_h])
for x in range(img_w):
    #if x % 4 < 2:
        for y in range(img_h):
                img[x, y] = 1
fov_deg = (11.42, 11.42)
ret = projector_by_image(fov_deg, img, projector_name = tmp_projector_name)
with open(tmp_projector_name + '.inc', 'w') as f:
    f.write(ret)
#print(ret)
#####

#####
tmp_projector_name = 'projector_full_low_res'
img_w = 16
img_h = 16
img = np.zeros([img_w,img_h])
for x in range(img_w):
    #if x % 4 < 2:
        for y in range(img_h):
                img[x, y] = 1
fov_deg = (11.42, 11.42)
ret = projector_by_image(fov_deg, img, projector_name = tmp_projector_name)
with open(tmp_projector_name + '.inc', 'w') as f:
    f.write(ret)
#####

#####
tmp_projector_name = 'projector_full_128_128'
img_w = 128
img_h = 128
img = np.zeros([img_w,img_h])
for x in range(img_w):
    #if x % 4 < 2:
        for y in range(img_h):
                img[x, y] = 1
fov_deg = (11.42, 11.42)
ret = projector_by_image(fov_deg, img, projector_name = tmp_projector_name)
with open(tmp_projector_name + '.inc', 'w') as f:
    f.write(ret)
#####

#####
tmp_projector_name = 'projector_full_256_256'
img_w = 256
img_h = 256
img = np.zeros([img_w,img_h])
for x in range(img_w):
    #if x % 4 < 2:
        for y in range(img_h):
                img[x, y] = 1
fov_deg = (11.42, 11.42)
ret = projector_by_image(fov_deg, img, projector_name = tmp_projector_name)
with open(tmp_projector_name + '.inc', 'w') as f:
    f.write(ret)
#####

#####
tmp_projector_name = 'projector_256_256_mod_y_256_lt_128'
img_w = 256
img_h = 256
img = np.zeros([img_w,img_h])
for x in range(img_w):
    #if x % 4 < 2:
        for y in range(img_h):
            if y % 256 < 128:
                img[x, y] = 1
fov_deg = (11.42, 11.42)
ret = projector_by_image(fov_deg, img, projector_name = tmp_projector_name)
with open(tmp_projector_name + '.inc', 'w') as f:
    f.write(ret)
#####
#####
tmp_projector_name = 'projector_256_256_mod_y_128_lt_64'
img_w = 256
img_h = 256
img = np.zeros([img_w,img_h])
for x in range(img_w):
    #if x % 4 < 2:
        for y in range(img_h):
            if y % 128 < 64:
                img[x, y] = 1
fov_deg = (11.42, 11.42)
ret = projector_by_image(fov_deg, img, projector_name = tmp_projector_name)
with open(tmp_projector_name + '.inc', 'w') as f:
    f.write(ret)
#####
#####
tmp_projector_name = 'projector_256_256_mod_y_64_lt_32'
img_w = 256
img_h = 256
img = np.zeros([img_w,img_h])
for x in range(img_w):
    #if x % 4 < 2:
        for y in range(img_h):
            if y % 64 < 32:
                img[x, y] = 1
fov_deg = (11.42, 11.42)
ret = projector_by_image(fov_deg, img, projector_name = tmp_projector_name)
with open(tmp_projector_name + '.inc', 'w') as f:
    f.write(ret)
#####
#####
tmp_projector_name = 'projector_256_256_mod_y_32_lt_16'
img_w = 256
img_h = 256
img = np.zeros([img_w,img_h])
for x in range(img_w):
    #if x % 4 < 2:
        for y in range(img_h):
            if y % 32 < 16:
                img[x, y] = 1
fov_deg = (11.42, 11.42)
ret = projector_by_image(fov_deg, img, projector_name = tmp_projector_name)
with open(tmp_projector_name + '.inc', 'w') as f:
    f.write(ret)
#####
#####
tmp_projector_name = 'projector_256_256_mod_y_16_lt_8'
img_w = 256
img_h = 256
img = np.zeros([img_w,img_h])
for x in range(img_w):
    #if x % 4 < 2:
        for y in range(img_h):
            if y % 16 < 8:
                img[x, y] = 1
fov_deg = (11.42, 11.42)
ret = projector_by_image(fov_deg, img, projector_name = tmp_projector_name)
with open(tmp_projector_name + '.inc', 'w') as f:
    f.write(ret)
#####
#####
tmp_projector_name = 'projector_256_256_mod_y_8_lt_4'
img_w = 256
img_h = 256
img = np.zeros([img_w,img_h])
for x in range(img_w):
    #if x % 4 < 2:
        for y in range(img_h):
            if y % 8 < 4:
                img[x, y] = 1
fov_deg = (11.42, 11.42)
ret = projector_by_image(fov_deg, img, projector_name = tmp_projector_name)
with open(tmp_projector_name + '.inc', 'w') as f:
    f.write(ret)
#####
#####
tmp_projector_name = 'projector_256_256_mod_y_4_lt_2'
img_w = 256
img_h = 256
img = np.zeros([img_w,img_h])
for x in range(img_w):
    #if x % 4 < 2:
        for y in range(img_h):
            if y % 4 < 2:
                img[x, y] = 1
fov_deg = (11.42, 11.42)
ret = projector_by_image(fov_deg, img, projector_name = tmp_projector_name)
with open(tmp_projector_name + '.inc', 'w') as f:
    f.write(ret)
#####
#####
tmp_projector_name = 'projector_256_256_mod_y_2_lt_1'
img_w = 256
img_h = 256
img = np.zeros([img_w,img_h])
for x in range(img_w):
    #if x % 4 < 2:
        for y in range(img_h):
            if y % 2 < 1:
                img[x, y] = 1
fov_deg = (11.42, 11.42)
ret = projector_by_image(fov_deg, img, projector_name = tmp_projector_name)
with open(tmp_projector_name + '.inc', 'w') as f:
    f.write(ret)
#####
#####
tmp_projector_name = 'projector_256_256_mod_x_256_lt_128'
img_w = 256
img_h = 256
img = np.zeros([img_w,img_h])
for x in range(img_w):
    if x % 256 < 128:
        for y in range(img_h):
            #if y % 256 < 128:
                img[x, y] = 1
fov_deg = (11.42, 11.42)
ret = projector_by_image(fov_deg, img, projector_name = tmp_projector_name)
with open(tmp_projector_name + '.inc', 'w') as f:
    f.write(ret)
#####
#####
tmp_projector_name = 'projector_256_256_mod_x_128_lt_64'
img_w = 256
img_h = 256
img = np.zeros([img_w,img_h])
for x in range(img_w):
    if x % 128 < 64:
        for y in range(img_h):
            #if y % 256 < 128:
                img[x, y] = 1
fov_deg = (11.42, 11.42)
ret = projector_by_image(fov_deg, img, projector_name = tmp_projector_name)
with open(tmp_projector_name + '.inc', 'w') as f:
    f.write(ret)
#####
#####
tmp_projector_name = 'projector_256_256_mod_x_64_lt_32'
img_w = 256
img_h = 256
img = np.zeros([img_w,img_h])
for x in range(img_w):
    if x % 64 < 32:
        for y in range(img_h):
            #if y % 256 < 128:
                img[x, y] = 1
fov_deg = (11.42, 11.42)
ret = projector_by_image(fov_deg, img, projector_name = tmp_projector_name)
with open(tmp_projector_name + '.inc', 'w') as f:
    f.write(ret)
#####
#####
tmp_projector_name = 'projector_256_256_mod_x_32_lt_16'
img_w = 256
img_h = 256
img = np.zeros([img_w,img_h])
for x in range(img_w):
    if x % 32 < 16:
        for y in range(img_h):
            #if y % 256 < 128:
                img[x, y] = 1
fov_deg = (11.42, 11.42)
ret = projector_by_image(fov_deg, img, projector_name = tmp_projector_name)
with open(tmp_projector_name + '.inc', 'w') as f:
    f.write(ret)
#####
#####
tmp_projector_name = 'projector_256_256_mod_x_16_lt_8'
img_w = 256
img_h = 256
img = np.zeros([img_w,img_h])
for x in range(img_w):
    if x % 16 < 8:
        for y in range(img_h):
            #if y % 256 < 128:
                img[x, y] = 1
fov_deg = (11.42, 11.42)
ret = projector_by_image(fov_deg, img, projector_name = tmp_projector_name)
with open(tmp_projector_name + '.inc', 'w') as f:
    f.write(ret)
#####
#####
tmp_projector_name = 'projector_256_256_mod_x_8_lt_4'
img_w = 256
img_h = 256
img = np.zeros([img_w,img_h])
for x in range(img_w):
    if x % 8 < 4:
        for y in range(img_h):
            #if y % 256 < 128:
                img[x, y] = 1
fov_deg = (11.42, 11.42)
ret = projector_by_image(fov_deg, img, projector_name = tmp_projector_name)
with open(tmp_projector_name + '.inc', 'w') as f:
    f.write(ret)
#####
#####
tmp_projector_name = 'projector_256_256_mod_x_4_lt_2'
img_w = 256
img_h = 256
img = np.zeros([img_w,img_h])
for x in range(img_w):
    if x % 4 < 2:
        for y in range(img_h):
            #if y % 256 < 128:
                img[x, y] = 1
fov_deg = (11.42, 11.42)
ret = projector_by_image(fov_deg, img, projector_name = tmp_projector_name)
with open(tmp_projector_name + '.inc', 'w') as f:
    f.write(ret)
#####
#####
tmp_projector_name = 'projector_256_256_mod_x_2_lt_1'
img_w = 256
img_h = 256
img = np.zeros([img_w,img_h])
for x in range(img_w):
    if x % 2 < 1:
        for y in range(img_h):
            #if y % 256 < 128:
                img[x, y] = 1
fov_deg = (11.42, 11.42)
ret = projector_by_image(fov_deg, img, projector_name = tmp_projector_name)
with open(tmp_projector_name + '.inc', 'w') as f:
    f.write(ret)
#####