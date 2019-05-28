#coding=utf-8

import numpy as np
import cv2
import json
import os 

output = "./crop_img"
source = "/mnt/md126/zhangjunyi/drone-object-detection/data/VOC2007/JPEGImages"
crop_txt = "./crop_txt"
source_txt = "/mnt/md126/zhangjunyi/drone-object-detection/data/VOC2007/txt"

if not os.path.exists(output):
   os.mkdir(output)

if not os.path.exists(crop_txt):
   os.mkdir(crop_txt)

with open('/mnt/md126/zhangjunyi/drone-object-detection/prop.json', 'r') as f:
        data = json.load(f)

bbox_list = data['bbox']
name_list = data['img_name']

#data_new = data.copy()
def get_label_bbox(txt_path):
    f = open(txt_path)
    lines = f.readlines()
    n = len(lines)
    #print("n:", n)
    bbox = [[] for i in range(n)]
    for line in lines:
        #print("line index:", lines.index(line))
        #print("line:", line)
        line_cp = line
        line = line.strip()
        label = line.split(",")
        x1 = int(label[0])
        y1 = int(label[1])
        x2 = int(label[0]) + int(label[2])
        y2 = int(label[1]) + int(label[3])
        bbox[lines.index(line_cp)] = [x1,y1,x2,y2]
    #print(bbox)
    return np.array(bbox)

def get_new_label(label_bbox, x1,y1,x2,y2):
    print(label_bbox.shape)
    #筛选早范围内的标签
    p = 3
    new_label = label_bbox[(label_bbox[:,0] + p > x1) & (label_bbox[:,1] + p > y1) & (label_bbox[:,2] - p < x2) & (label_bbox[:,3] - p < y2)]
    print(new_label.shape)
    #计算相对坐标
    new_label[:,0] = new_label[:,0] - x1 + 1
    new_label[:,1] = new_label[:,1] - y1 + 1
    new_label[:,2] = new_label[:,2] - x1 + 1 
    new_label[:,3] = new_label[:,3] - y1 + 1
    print(new_label)   
     
    print(new_label)   
    return new_label


for i in name_list:
    
    name = i.split(".")[0]
    #print("name:", name)
    path = os.path.join(source,i)
    #print("path:", path)
    im = cv2.imread(path)
 
    #print("region_bbox:", bbox_list[name_list.index(i)])
    region_bbox = bbox_list[name_list.index(i)]
    count = 0
    txt_path = os.path.join(source_txt, name+".txt")
    label_bbox = get_label_bbox(txt_path)
 
    for j in region_bbox:
        new_name = name + "_" + str(count) + ".jpg" 
        print(new_name)
        x1 = int(j[0])
        y1 = int(j[1])
        x2 = int(j[2])
        y2 = int(j[3])
        im_crop = im[y1:y2, x1:x2]
        cv2.imwrite(os.path.join(output,new_name), im_crop)
        count = count + 1
        label = get_new_label(label_bbox, x1,y1,x2,y2)       
#region_box = bbox[0]
#print("name:", name)
#print("region_box:", region_box)
    break




