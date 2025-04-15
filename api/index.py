from flask import Flask, jsonify, request
import tflite_runtime.interpreter as tflite
import logging

app = Flask(__name__)

interpreter = tflite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

@app.route("/")
def home():
    return 'Hello, World! :)'

@app.route("/predict", methods=["POST"])
def predict():
    logging.debug("model loaded!")
    return 'Prediction coming'
