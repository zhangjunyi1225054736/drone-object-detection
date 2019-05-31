
import json
import os


class_txt = "./class.txt"


with open('/mnt/md126/zhangjunyi/365-object-detection/VOC2007/cocoformatJson/voc_2007_test.json', 'r') as f:
     data = json.load(f)

categories = data['categories']

#print(categories)

def get_category_id(name):
    #print(name)
    #category_id = list(categories.keys())[list(categories.values()).index(name)]  
    for i in categories:
        if i["name"] == name:
           category_id = i["id"]
           break
        else:
           pass
    #print(category_id)
    return category_id

f1 = open(class_txt)



result = []

f1_lines = f1.readlines()


for filename in f1_lines:
    filename = filename.strip()
    class_name = filename.split("_")[4].split(".")[0]
    category_id = get_category_id(class_name)
    #print(file_name)
    #exit()
    f3 = open("./test_result/"+filename)
    f3_lines = f3.readlines()
    for line in f3_lines:
        d = {}
        line = line.strip().split()
        image_id = line[0].split("_")[2]
        image_id = int(image_id)
        score = float(line[1])
        x = float(line[2])
        y = float(line[3])
        w = round((float(line[4]) - float(line[2])),1)
        h = round((float(line[5]) - float(line[3])),1)
        bbox = [x,y,w,h]
        d["image_id"] = image_id
        d["category_id"] = category_id
        d["bbox"] = bbox
        d["score"] = score
        result.append(d)
        #print(result)
        #break


f_json = open('result.json','w',encoding='utf-8')

str_json=json.dump(result,f_json)

#print(str_json)
