import tensorflow as tf
from tensorflow import keras


class DigitRecognitionModel:
    def __init__(self):
        self.model = keras.Sequential()

    def build_model(self):
        # First Convolution Layer
        self.model.add(keras.layers.Conv2D(64, (3, 3), input_shape = (28, 28, 1)))
        self.model.add(keras.layers.Activation("relu"))
        self.model.add(keras.layers.MaxPooling2D(pool_size =(2, 2)))

        # 2nd Convolution Layer
        self.model.add(keras.layers.Conv2D(64, (3, 3)))
        self.model.add(keras.layers.Activation("relu"))
        self.model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))

         # 3nd Convolution Layer
        self.model.add(keras.layers.Conv2D(64, (3, 3)))
        self.model.add(keras.layers.Activation("relu"))
        self.model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))

        # Fully Connected Layer
        self.model.add(keras.layers.Flatten())
        self.model.add(keras.layers.Dense(64))
        self.model.add(keras.layers.Activation("relu"))

        # Fully Connected Layer2
        self.model.add(keras.layers.Dense(32))
        self.model.add(keras.layers.Activation("relu"))

        # Last FUlly Connected Layer
        self.model.add(keras.layers.Dense(10))
        self.model.add(keras.layers.Activation("softmax"))

    def compile_model(self):
            self.model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        
    def train_model(self, x_trainr, y_train, epochs=5, validation_split = 0.3):
            self.model.fit(x_trainr, y_train, epochs=epochs, validation_split=validation_split)

    def evaluate_model(self, x_testr, y_test):
            test_loss, test_acc = self.model.evaluate(x_testr, y_test)
            return test_loss, test_acc
    def predict(self, x):
            predictions = self.model.predict(x)
            return predictions
    def save_model(self, Path):
          self.model.save(Path)