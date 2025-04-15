from flask import Flask, jsonify, request
import tensorflow as tf
import logging

app = Flask(__name__)

interpreter = tflite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

@app.route("/")
def home():
    return 'Hello, World! :)'

@app.route("/predict")
def predict():
    model = tf.keras.models.load_model('api/model/test_model_00.keras')
    logging.debug("model loaded!")
    return 'Prediction coming'
