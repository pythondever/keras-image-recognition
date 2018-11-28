import configparser

cf = configparser.ConfigParser()
cf.read("/home/fantasy/MachineLearning/project/spiders/recognition/config/project.config")

def get_option(section, name):
    """
    获取参数
    """
    return cf.get(section, name)