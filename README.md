# keras-image-recognition
keras 图像识别

## python版本 
Python 3.4.5

## keras 版本
2.2.2

## tensoflow 版本
1.9.0

## os
linux

## 使用keras + tensorflow + cpu 进行图像识别
识别的类型有三种：猫，狗，马
项目运行需要解压 downloads 目录下面的 test.tar.gz 和 train.tar.gz
需要安装依赖包
pip install -r requirements.txt

## 运行项目
cd spiders/recognition/train
python train.py

## 识别图像
cd spiders/prediction
python prediction.py -i ./data/20181128094323.jpg -m ../classify.model







