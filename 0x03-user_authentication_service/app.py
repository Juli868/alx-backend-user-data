#!/usr/bin/env python3
"""Run my application on a web."""
from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/")
def home():
    """Page for home."""
    return jsonify({"message": "Bienvenue"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
