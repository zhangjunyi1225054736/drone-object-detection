#!/bin/bash

#n is the number od test images
n=548
#step is the iteration step of the trained model
step=39999

cuda=5

rm -rf /home/zhangdongyu/object-detection/detectron/VOC2007/VOCdevkit2007/annotations_cache

cp /home/zhangdongyu/object-detection/detectron/VOC2007/ImageSets/Main/test_$n.txt /home/zhangdongyu/object-detection/detectron/VOC2007/ImageSets/Main/zjy/test.txt
cp /home/zhangdongyu/object-detection/detectron/VOC2007/ImageSets/Main/test_$n.txt /home/zhangdongyu/object-detection/detectron/VOC2007/ImageSets/Main/test.txt
 
python ./tools/pascal_voc_xml2coco_json_converter_zjy.py ./data/ 2007

#CUDA_VISIBLE_DEVICES=$cuda python tools/test_net.py --dataset voc2007 --cfg configs/baselines/e2e_mask_rcnn_X-152-32x8d-FPN-IN5k_1.44x.yaml \
         #--load_ckpt Outputs/e2e_mask_rcnn_X-152-32x8d-FPN-IN5k_1.44x/Apr28-14-53-17_zdyhpc_step/ckpt/model_step$step.pth --vis #--multi-gpu-testing

CUDA_VISIBLE_DEVICES=$cuda python tools/test_net.py --dataset voc2007 --cfg configs/baselines/e2e_mask_rcnn_X-152-32x8d-FPN-IN5k_1.44x.yaml \
         --load_ckpt ./Outputs/voc2007/e2e_mask_rcnn_X-152-32x8d-FPN-IN5k_1.44x/May13-14-27-31_zdyhpc_step/ckpt/model_step$step.pth #--vis #--multi-gpu-testing

