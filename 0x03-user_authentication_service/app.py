#!/usr/bin/env python3
"""Run my application on a web."""
from flask import Flask, jsonify
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route("/")
def home():
    """Page for home."""
    return jsonify({"message": "Bienvenue"})

@app.route("/users/", methods=['POST'])
def users():
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        jsonify('"\{email": "{}", "message": "user created"\}'.format(email))
    except ValueError:
        return jsonify('\{"message": "email already registered"\}'), 400


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
