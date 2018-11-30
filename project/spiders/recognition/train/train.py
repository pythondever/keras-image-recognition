import os
import sys
import smtplib
sys.path.append("../")
import numpy as np
from keras.utils import plot_model
import matplotlib.pyplot as plt
from keras.optimizers import Adam
from model.model import ImageModel
from email.mime.text import MIMEText
from keras.callbacks import EarlyStopping
from config.get_arguments import get_option
from keras.callbacks import ModelCheckpoint
from image_matrix import image_matrix, image_label
from keras.preprocessing.image import ImageDataGenerator


def run(train_path, test_path):
    """
    训练模型
    """
    height = int(get_option("image", "height"))
    width = int(get_option("image", "width"))
    classes = int(get_option("image", "classes"))
    epochs = int(get_option("train", "epochs"))
    batch_size = int(get_option("train", "batch_size"))
    save_path = get_option("model", "save_path")

    model = ImageModel.build(width=width, heigth=height, classes=classes)
    # init_lr = 0.001
    init_lr = 1e-3
    decay=0.0
    opt = Adam(lr=init_lr, decay=decay)
    # adam = Adam(lr=0.001, beta_1=0.99,beta_2=0.9, epsilon=1e-8)
    # 编译模型需要三个参数， 优化器，损失函数，指标列表
    model.compile(optimizer=opt, loss="categorical_crossentropy", metrics=['accuracy'])
    train_matrix = image_matrix(train_path)
    train_label = image_label(train_path)
    test_matrix = image_matrix(test_path)
    test_label = image_label(test_path)
    # 图像预处理， rotation range的作用是用户指定旋转角度范围
    # width_shift_range & height_shift_range 分别是水平位置平移和上下位置平移
    # horizontal_flip的作用是随机对图片执行水平翻转操作
    datagen = ImageDataGenerator(
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True)
    if os.path.exists('checkpoint.chk'):
        model.load_weights("checkpoint.chk")
    result = model.fit_generator(
        datagen.flow(train_matrix, train_label, batch_size=batch_size), 
        validation_data=(test_matrix, test_label),
        # steps_per_epoch = len(train_matrix) // epochs,
        epochs=epochs,
        verbose=1,
        # callbacks=[EarlyStopping(monitor='val_loss', min_delta=0, patience=5, verbose=0, mode='auto')]
        callbacks = [ModelCheckpoint('checkpoint.chk', monitor='val_loss', 
        verbose=0, save_best_only=True, save_weights_only=False, mode='auto', period=1)]
        )
    score = model.evaluate(test_matrix, test_label, batch_size=32)
    print("训练完毕 模型评分 %s" % score)
    model.save(save_path)
    plot_model(model, to_file='model.png')
    plt.style.use("ggplot")
    plt.figure()
    n = epochs
    aranges = np.arange(0, n)
    plt.plot(result.history["loss"], label="train_loss")
    plt.plot(result.history["acc"], label="train_acc")
    plt.plot(result.history["val_loss"], label="val_loss")
    plt.plot(result.history["val_acc"], label="val_acc")

    plt.title("Image recognition")
    plt.xlabel("Epochs")
    plt.ylabel("loss/acc")
    plt.legend(loc="lower left")
    plt.savefig("reco")
    tellMeResult(score)

def tellMeResult(result):
    """
    训练完毕，发送邮件告诉我结果
    """
    host = get_option('email', 'host')
    account = get_option('email', 'account')
    key = get_option('email', 'key')
    target = get_option('email', 'recv_account')
    title = get_option('email', 'title')
    result = '模型的准确率: ' + str(int(result[1] * 100))
    msg = MIMEText(result)
    msg['Subject'] = title
    msg['From'] = account
    msg['To'] = target
    try:
        smtp = smtplib.SMTP_SSL()
        smtp.connect(host=host)
        smtp.login(account, key)
        smtp.sendmail(account, target, msg.as_string())
    except Exception as ex:
        print('邮件发送失败： %s' % ex)


if __name__ == "__main__":
    train = get_option("data_set", "train_data")
    test = get_option("data_set", "test_data")
    run(train, test)
