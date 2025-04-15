from flask import Flask, jsonify
from werkzeug.wrappers import Request, Response

app = Flask(__name__)

@app.route("/")
def home():
    return 'Hello, World! :)'

@app.route("/predict")
def predict():
    return 'Prediction coming soon'
