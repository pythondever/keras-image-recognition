import os
import cv2
import sys
import imutils
import argparse
import numpy as np
sys.path.append('../')
from keras import backend as K
import matplotlib.pyplot as plt
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from recognition.config.get_arguments import get_option

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

def view_layer(model, image_data):
    """
    获取卷积层的输出
    """
    print('============== 中间层输出 ==============')
    # 第一个 model.layers[0],不修改,表示输入数据；第二个model.get_layer 你需要给自己的layer 命名才能获取到
    layer_1 = K.function([model.layers[0].input], [model.get_layer('filter1').output])
    f1 = layer_1([image_data])[0] # 只修改inpu_image
    # 第一层卷积后的特征图展示（样本个数，特征图尺寸长，特征图尺寸宽，特征图个数）
    height = layer_1.outputs[0].shape[1]
    width = layer_1.outputs[0].shape[2]
    filterCount = layer_1.outputs[0].shape[-1]
    print('filter1 图片 大小 %s x %s 核心数量 %s' % (height, width, filterCount))
    # filterCount 表示filter个数
    for _ in range(filterCount):
        show_img = f1[:, :, :, _]
        show_img.shape = [height, width]
        # subplot 定义 8 行 8 列的小图
        plt.subplot(8, 8, _ + 1)
        plt.imshow(show_img, cmap='jet')
        plt.axis('off')
    plt.show()
    layer_1 = K.function([model.layers[0].input], [model.get_layer('max1').output])
    f1 = layer_1([image_data])[0] # 只修改inpu_image
    # 第一层卷积后的特征图展示（样本个数，特征图尺寸长，特征图尺寸宽，特征图个数）
    height = layer_1.outputs[0].shape[1]
    width = layer_1.outputs[0].shape[2]
    filterCount = layer_1.outputs[0].shape[-1]
    print('pooling1 图片 大小 %s x %s 核心数量 %s' % (height, width, filterCount))
    # filterCount 表示filter个数
    for _ in range(filterCount):
        show_img = f1[:, :, :, _]
        show_img.shape = [height, width]
        # subplot 定义 8 行 8 列的小图
        plt.subplot(8, 8, _ + 1)
        plt.imshow(show_img, cmap='jet')
        plt.axis('off')
    plt.show()
    # --------------------------------------------------------------------------------
    layer_1 = K.function([model.layers[0].input], [model.get_layer('filter2').output])
    f1 = layer_1([image_data])[0] # 只修改inpu_image
    # 第一层卷积后的特征图展示（样本个数，特征图尺寸长，特征图尺寸宽，特征图个数）
    height = layer_1.outputs[0].shape[1]
    width = layer_1.outputs[0].shape[2]
    filterCount = layer_1.outputs[0].shape[-1]
    print('filter2 图片 大小 %s x %s 核心数量 %s' % (height, width, filterCount))
    # filterCount 表示filter个数
    for _ in range(filterCount):
        show_img = f1[:, :, :, _]
        show_img.shape = [height, width]
        # subplot 定义 8 行 8 列的小图
        plt.subplot(8, 8, _ + 1)
        plt.imshow(show_img, cmap='jet')
        plt.axis('off')
    plt.show()

    layer_1 = K.function([model.layers[0].input], [model.get_layer('max2').output])
    f1 = layer_1([image_data])[0] # 只修改inpu_image
    # 第一层卷积后的特征图展示（样本个数，特征图尺寸长，特征图尺寸宽，特征图个数）
    height = layer_1.outputs[0].shape[1]
    width = layer_1.outputs[0].shape[2]
    filterCount = layer_1.outputs[0].shape[-1]
    print('pooling2 图片 大小 %s x %s 核心数量 %s' % (height, width, filterCount))
    # filterCount 表示filter个数
    for _ in range(filterCount):
        show_img = f1[:, :, :, _]
        show_img.shape = [height, width]
        # subplot 定义 8 行 8 列的小图
        plt.subplot(8, 8, _ + 1)
        plt.imshow(show_img, cmap='jet')
        plt.axis('off')
    plt.show()
    # -------------------------------------------------------------------------------
    layer_1 = K.function([model.layers[0].input], [model.get_layer('filter3').output])
    f1 = layer_1([image_data])[0] # 只修改inpu_image
    # 第一层卷积后的特征图展示（样本个数，特征图尺寸长，特征图尺寸宽，特征图个数）
    height = layer_1.outputs[0].shape[1]
    width = layer_1.outputs[0].shape[2]
    filterCount = layer_1.outputs[0].shape[-1]
    print('filter3 图片 大小 %s x %s 核心数量 %s' % (height, width, filterCount))
    # filterCount 表示filter个数
    for _ in range(filterCount):
        show_img = f1[:, :, :, _]
        show_img.shape = [height, width]
        # subplot 定义 8 行 8 列的小图
        plt.subplot(8, 8, _ + 1)
        plt.imshow(show_img, cmap='jet')
        plt.axis('off')
    plt.show()
    # ----------------------------------------------------------------------------
    layer_1 = K.function([model.layers[0].input], [model.get_layer('max3').output])
    f1 = layer_1([image_data])[0] # 只修改inpu_image
    # 第一层卷积后的特征图展示（样本个数，特征图尺寸长，特征图尺寸宽，特征图个数）
    height = layer_1.outputs[0].shape[1]
    width = layer_1.outputs[0].shape[2]
    filterCount = layer_1.outputs[0].shape[-1]
    print('pooling3 图片 大小 %s x %s 核心数量 %s' % (height, width, filterCount))
    # filterCount 表示filter个数
    for _ in range(filterCount):
        show_img = f1[:, :, :, _]
        show_img.shape = [height, width]
        # subplot 定义 8 行 8 列的小图
        plt.subplot(8, 8, _ + 1)
        plt.imshow(show_img, cmap='jet')
        plt.axis('off')
    plt.show()


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
    view_layer(model, image)


if __name__ == "__main__":
    predict()
