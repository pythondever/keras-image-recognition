import os
import cv2
import sys
import imutils
import argparse
import numpy as np
sys.path.append('../')
from recognition.config.get_arguments import get_option
from keras.models import load_model
from keras.preprocessing.image import img_to_array

# 根据已有的模型预测单张图片是属于哪个类型

def getArgs():
    """
    获取输入参数
    """
    ag = argparse.ArgumentParser()
    ag.add_argument("-i", "--image", required=True, help="input image" )
    ag.add_argument("-m", "--model", required=True, help="input model")
    ag.add_argument("-s", "--show", action="store_true", default=False, help="show predict result")

    args = vars(ag.parse_args())
    return args

def image_array(input_image):
    """
    讲图片数据转换为array
    """
    height = int(get_option("image", "height"))
    width = int(get_option("image", "width"))
    image = cv2.imread(input_image)
    image = cv2.resize(image, (height, width))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    return image


def predict():
    """
    预测图片属于那种类型
    """

    arg = getArgs()
    model = arg["model"]
    input_image = arg["image"]

    if not os.path.exists(input_image):
        print('预测失败,图片不存在 %s' % input_image)
        return 
    if not os.path.exists(model):
        print("预测失败， model不存在 %s" % model)
    
    image = image_array(input_image)
    orgin = {0:"猫",1:"狗", 2:"马"}
    model = load_model(model)
    result = model.predict(image)[0]
    proba = np.max(result)
    label = str(np.where(result==proba)[0])
    label = "{}".format(label)
    closed = "{:.2f}%".format(proba * 100)
    label = eval(label)
    print("该图片有 %s 的可能性是属于 %s 类别" % (closed, orgin.get(label[0])))


if __name__ == "__main__":
    predict()