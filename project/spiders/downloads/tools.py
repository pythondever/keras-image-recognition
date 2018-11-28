import os
import hashlib
from imutils import paths

# 图片过滤

def get_md5(filename):
    """
    获取文件的MD5
    """
    md5 = os.popen('md5sum %s' % filename).read().split(' ')[0]
    return md5

def filterAll(path):
    """

    """
    if not os.path.exists(path):
        print('过滤失败,路径不存在')
        return 
    hash = dict()
    images = paths.list_images(path)
    for im in images:
        md5 = get_md5(im)
        filename = os.path.basename(im)
        if md5 not in hash:
            hash[md5] = filename
        else:
            name = hash.get(md5)
            print('图片重复 %s 和 %s' % (im, name))
            os.system('rm -rf %s' % im)

def renameImage(path):
    """
    """
    images = paths.list_images(path)

    for im in images:
        md5 = get_md5(im)
        filePath = os.path.join(path, md5)
        os.system('mv %s %s' % (im, filePath))



filterAll('/home/fantasy/MachineLearning/project/spiders/downloads')
renameImage('/home/fantasy/MachineLearning/project/spiders/downloads/猫图片')


