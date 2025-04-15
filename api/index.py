from flask import Flask, jsonify, request
import tensorflow as tf

app = Flask(__name__)

@app.route("/")
def home():
    return 'Hello, World! :)'

@app.route("/predict")
def predict():
    # model = tf.keras.models.load_model('api/model/test_model_00.keras')
    return 'Prediction coming'
