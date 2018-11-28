import os
import sys
import cv2
import numpy as np
from imutils import paths
from keras.utils import to_categorical
from config.get_arguments import get_option
from keras.preprocessing.image import img_to_array


def image2matrix(path):
    """
    图像裁剪然后转为矩阵
    """
    heigth = int(get_option("image", "height"))
    width = int(get_option("image", "width"))
    matrix = list()
    labels = []
    if os.path.exists(path) is False:
        print("路径不存在 %s" % path)
        return 
    images = paths.list_images(path)
    for img in images:
        image = cv2.imread(img)
        # 有时候读取文件会返回None 不知道为什么读取不到因此这里先这样处理
        if image is None:
            os.system('rm -rf %s' % img)
            continue
        cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        try:
            image = cv2.resize(image, (heigth, width), interpolation = cv2.INTER_AREA)
            image = img_to_array(image)
        except Exception as ex:
            print(ex)
            print(img)
            sys.exit(1)
        matrix.append(image)
        label = int(img.split(os.path.sep)[-2])
        labels.append(label)

    return matrix, labels

def image_matrix(path):
    """
    训练集矩阵
    """
    matrix, _ = image2matrix(path)
    matrix = np.array(matrix, dtype="float") / 255.0
    return matrix

def image_label(path):
    """
    训练集标签
    """
    classes = int(get_option("image", 'classes'))
    _, labels = image2matrix(path)
    labels = np.array(labels)
    labels = to_categorical(labels, num_classes=classes)

    return labels


