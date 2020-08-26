# encoding=utf-8

from keras.datasets import mnist
from keras.layers.core import Dense
from keras.models import Sequential
from keras.optimizers import SGD
from keras.utils import np_utils


def load_data():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    number = 10000
    x_train = x_train[0:number]
    y_train = y_train[0:number]
    x_train = x_train.reshape(number, 28 * 28)
    x_test = x_test.reshape(x_test.shape[0], 28 * 28)
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    y_train = np_utils.to_categorical(y_train, 10)
    y_test = np_utils.to_categorical(y_test, 10)
    x_train = x_train / 255
    x_test = x_test / 255
    return (x_train, y_train), (x_test, y_test)


def create_model():
    (x_train, y_train), (x_test, y_test) = load_data()

    model = Sequential()
    model.add(Dense(input_dim=28 * 28, units=689, activation='sigmoid'))
    model.add(Dense(units=689, activation='sigmoid'))
    model.add(Dense(units=689, activation='sigmoid'))
    model.add(Dense(units=10, activation='sigmoid'))

    model.compile(loss='mse', optimizer=SGD(lr=0.1), metrics=['accuracy'])

    model.fit(x_train, y_train, batch_size=100, epochs=20)

    result = model.evaluate(x_test, y_test)
    print("Test Acc:", result[1])


if __name__ == '__main__':
    create_model()
