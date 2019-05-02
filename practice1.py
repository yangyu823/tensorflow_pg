#!/Users/723310/anaconda3/bin

import tensorflow as tf

#Load and prepare the [MNIST](http://yann.lecun.com/exdb/mnist/) dataset. Convert the samples from integers to floating-point numbers:

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

#Build the `tf.keras` model by stacking layers. Select an optimizer and loss function used for training:


model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#Train and evaluate model:
print('Train and evaluate model:')

model.fit(x_train, y_train, epochs=5)

model.evaluate(x_test, y_test)