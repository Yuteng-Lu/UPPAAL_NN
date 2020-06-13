from keras.datasets import mnist
import numpy as np
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD

(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

print(np.shape(X_train), np.shape(X_test))

X_train = X_train.reshape(60000, 28*28)
X_test = X_test.reshape(10000, 28*28)

print(np.shape(X_train), np.shape(X_test))

X_train = X_train.astype("float32")
X_test = X_test.astype("float32")

# The value of each picture is at (0, 255) --> (0, 1): accelerates model training
X_train /= 255
X_test /= 255

num_classes = 10
Y_train = np_utils.to_categorical(Y_train, num_classes)
Y_test = np_utils.to_categorical(Y_test, num_classes)

model = Sequential()
model.add(Dense(5, input_shape=(784,))) # batch_size = 20, 30, 50, ...
model.add(Dense(3))
model.add(Dense(num_classes, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer=SGD(), metrics=['accuracy'])
model.fit(X_train, Y_train, batch_size=50, epochs=10, verbose=1, validation_data=(X_test, Y_test))
score = model.evaluate(X_test, Y_test, verbose=1)

for layer in model.layers:
    h = layer.get_weights()
    print(h)

weights = [layer.get_weights() for layer in model.layers]
# weights is the variable storing all the weights of trained DNN.
