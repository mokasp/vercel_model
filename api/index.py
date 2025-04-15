from flask import Flask, jsonify
from werkzeug.wrappers import Request, Response

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return jsonify({"message": "Hello from Flask on Vercel!"})

# Entry point for Vercel
def handler(environ, start_response):
    return app.wsgi_app(environ, start_response)
