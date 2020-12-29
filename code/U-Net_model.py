from keras.models import Model
from keras.engine.topology import Input
from keras.layers.core import Flatten, Dense, Reshape, Dropout, Activation
from keras.layers.convolutional import Conv2D, UpSampling2D
from keras.layers.pooling import MaxPooling2D
from keras.layers.merge import concatenate
from keras.layers.normalization import BatchNormalization


class UNet(object):
    def __init__(self, input_size):
        self.INPUT_SIZE = input_size

        inputs = Input((self.INPUT_SIZE, self.INPUT_SIZE, 3))
        print('this is the input shape', inputs.shape)

        encodeLayer1 = self.__add_encode_layers(64, inputs, is_first=True)
        encodeLayer2 = self.__add_encode_layers(128, encodeLayer1)
        encodeLayer3 = self.__add_encode_layers(256, encodeLayer2)
        encodeLayer4 = self.__add_encode_layers(512, encodeLayer3)
        encodeLayer5 = self.__add_encode_layers(1024, encodeLayer4)

        decodeLayer1 = self.__add_decode_layers(
            512, encodeLayer5, encodeLayer4)
        decodeLayer2 = self.__add_decode_layers(
            256, decodeLayer1, encodeLayer3, add_drop_layer=True)
        decodeLayer3 = self.__add_decode_layers(
            128, decodeLayer2, encodeLayer2, add_drop_layer=True)
        decodeLayer4 = self.__add_decode_layers(
            64, decodeLayer3, encodeLayer1)

        outputs = Conv2D(6, 1, activation='softmax')(decodeLayer4)
        print('this is the output shape', outputs.shape)

        self.MODEL = Model(inputs=[inputs], outputs=[outputs])

    def __add_encode_layers(self, filter_size, input_layer, is_first=False):
        layer = input_layer
        if is_first:
            layer = Conv2D(filter_size, 3, padding='same', input_shape=(
                self.INPUT_SIZE, self.INPUT_SIZE, 3))(layer)
        else:
            layer = MaxPooling2D(2)(layer)
            layer = Conv2D(filter_size, 3, padding='same')(layer)
        layer = Conv2D(filter_size, 3, padding='same')(layer)
        layer = BatchNormalization()(layer)
        layer = Activation(activation='relu')(layer)
        print(layer.shape)
        return layer

    def __add_decode_layers(self, filter_size, input_layer, concat_layer, add_drop_layer=False):
        layer = UpSampling2D(2)(input_layer)
        layer = concatenate([layer, concat_layer])
        layer = Conv2D(filter_size, 3, padding='same')(layer)
        layer = Conv2D(filter_size, 3, padding='same')(layer)
        layer = BatchNormalization()(layer)
        layer = Activation(activation='relu')(layer)
        if add_drop_layer:
            layer = Dropout(0.5)(layer)
        print(layer.shape)
        return layer

    def model(self):
        return self.MODEL
