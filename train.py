import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from model import DigitRecognitionModel

SAVE_MODEL_PATH = "models/digit_recog_models.h5"

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

## Normarlizing the data | Pre-Processing
x_train = tf.keras.utils.normalize(x_train, axis = 1)
x_test = tf.keras.utils.normalize(x_test, axis = 1)

## Resize image
IMG_SIZE = 28
x_trainr = np.array(x_train).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
x_testr = np.array(x_test).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

model = DigitRecognitionModel()
model.build_model()
model.compile_model()
model.train_model(x_trainr, y_train)

tf.saved_model(model, SAVE_MODEL_PATH)
predictions = model.predict([x_testr])
print(np.argmax(predictions[0]))