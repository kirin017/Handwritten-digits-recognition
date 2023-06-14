from flask import Flask, render_template, request, redirect, url_for, jsonify
import cv2
import tensorflow as tf
import numpy as np
from model import load_model
import gradio as gr
# Initialize Flask application
app = Flask(__name__)

IMG_SIZE = 28
SAVE_MODEL_PATH = "models/digit_recog_models.h5"

### Tải model
def get_model():
    global model 
    model = load_model(SAVE_MODEL_PATH)
### Xử lí ảnh trước khi đưa vào model
def preprocess_image(image_path, size = IMG_SIZE):
    image = cv2.imread(image_path)
    image = np.invert(np.array(image))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (28, 28), interpolation= cv2.INTER_AREA)
    newimg = newimg = tf.keras.utils.normalize (resized, axis = 1)
    newimg = np.array(newimg).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
    return newimg

get_model()
# Define route for the home page
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    image = request.files['imagefile']
    image_path = "./images/" + image.filename
    image.save(image_path)
    newimg = preprocess_image(image_path)
    prediction = model.predict(newimg)
    return render_template('index.html', pred=np.argmax(prediction))

def pre(image):
    image = request.files['imagefile']
    image_path = "./images/" + image.filename
    image.save(image_path)
    newimg = preprocess_image(image_path)
    pred = model.predict(newimg)
    return np.argmax(pred)


    # Trả về kết quả dự đoán
if __name__ == '__main__':
    app.run(port=3000, debug=True)
