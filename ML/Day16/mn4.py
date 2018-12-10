#keras imports for the dataset and building our neural network
import numpy
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.utils import np_utils
from keras.datasets import mnist

(X_train, y_train), (X_test, y_test) = mnist.load_data()

n_train, height, width = X_train.shape
n_test, _, _ = X_test.shape

n_train, n_test, height, width



from keras.utils.np_utils import to_categorical

# we have to preprocess the data into the right shape
X_train = X_train.reshape(n_train, height, width, 1).astype('float32')
X_test = X_test.reshape(n_test, height, width, 1).astype('float32')

# normalize from [0, 255] to [0, 1]
X_train /= 255
X_test /= 255

# numbers 0-9, so ten classes
n_classes = 10

# convert integer labels into one-hot vectors
y_train = to_categorical(y_train, n_classes)
y_test = to_categorical(y_test, n_classes)

# number of convolutional filters
n_filters = 32

# convolution filter size
# i.e. we will use a n_conv x n_conv filter
n_conv = 3

# pooling window size
# i.e. we will use a n_pool x n_pool pooling window
n_pool = 2

from keras.layers import Activation
from keras.layers.convolutional import Convolution2D, MaxPooling2D
model = Sequential()
model.add(Convolution2D(
        n_filters, 
        kernel_size=(n_conv, n_conv),
        # we have a 28x28 single channel (grayscale) image
        # so the input shape should be (28, 28, 1)
        input_shape=(height, width, 1)
))
model.add(Activation('relu'))

model.add(Convolution2D(n_filters, kernel_size=(n_conv, n_conv)))
model.add(Activation('relu'))

# then we apply pooling to summarize the features
# extracted thus far
model.add(MaxPooling2D(pool_size=(n_pool, n_pool)))

from keras.layers import Dropout, Flatten, Dense

model.add(Dropout(0.25))

# flatten the data for the 1D layers
model.add(Flatten())

# Dense(n_outputs)
model.add(Dense(128))
model.add(Activation('relu'))
model.add(Dropout(0.5))

# the softmax output layer gives us a probablity for each class
model.add(Dense(n_classes))
model.add(Activation('softmax'))


model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)


# how many examples to look at during each update step
batch_size = 128

# how many times to run through the full set of examples
n_epochs = 1

# the training may be slow depending on your computer
model.fit(X_train,
          y_train,
          batch_size=batch_size,
          epochs=n_epochs,
          validation_data=(X_test, y_test))



# how'd we do?
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)

print('loss:', loss)
print('accuracy:', accuracy)


x_sample = X_test[0].reshape(1,28,28,1)
y_prob = model.predict(x_sample)[0]
y_pred = y_prob.argmax()
y_actual = y_test[0].argmax()

print("probabilities: ", y_prob)
print("predicted = %d, actual = %d" % (y_pred, y_actual))
