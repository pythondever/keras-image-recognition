from keras import regularizers
from keras import backend as bk
from keras.models import Sequential
from keras.layers.core import Dense
from keras.layers.core import Flatten
from keras.layers.core import Dropout
from keras.layers.core import Activation
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.normalization import BatchNormalization


class ImageModel:
    @staticmethod
    def build(width, heigth, classes, depth=3):
        """

        """

        model = Sequential()
        if bk.image_data_format() == "channels_first":
            shape = (depth, width, heigth)

        else:
            shape = (width, heigth, depth)

        model.add(Conv2D(20, (3, 3), padding="same", input_shape=shape, name='filter1'))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(strides=(2, 2), name="max1"))
        model.add(Dropout(0.5))
        # ---------------------------------------------------------------
        model.add(Conv2D(30, (3, 3), padding="same", name='filter2'))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(strides=(2, 2), name="max2"))
        # ---------------------------------------------------------------
        model.add(Conv2D(50, (5, 5), padding="same", name='filter3'))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(strides=(2, 2), name="max3"))
        model.add(Dropout(0.5))
        # ---------------------------------------------------------------
        model.add(Flatten())
        # model.add(Dense(250, kernel_regularizer=regularizers.l2(0.01), activity_regularizer=regularizers.l1(0.01)))
        model.add(Dense(250))
        model.add(Dropout(0.5))
        model.add(Activation("relu"))
        # ---------------------------------------------------------------
        model.add(Dense(classes))
        model.add(Activation("softmax"))

        return model
