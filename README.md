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

## 训练/测试数据下载
链接：https://pan.baidu.com/s/1f1N01Qv5N6UouiOJS4ZCDg 
提取码：ycks 

链接：https://pan.baidu.com/s/1BSPDaqoQv_7kQifA9rbzMA 
提取码：k7ej 

下载完成后需要放到downloads 目录下面解压

## 使用keras + tensorflow + cpu 进行图像识别
识别的类型有三种：猫，狗，马
需要安装依赖包

pip install -r requirements.txt
模型的可视化需要安装graphviz

sudo apt-get install graphviz
或者
sudo yum install graphviz

## 运行项目
cd spiders/recognition/train

python train.py

## 识别图像
cd spiders/prediction

python prediction.py -i ./data/20181128094323.jpg -m ../classify.model

## 更多介绍
https://blog.csdn.net/lucky404/article/details/84581885







