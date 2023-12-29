#!/usr/bin/python3
"""A script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Returns a string for the index page"""

    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Router for page /hbnb"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
