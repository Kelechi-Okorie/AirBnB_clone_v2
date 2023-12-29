#!/usr/bin/python3
"""A script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Returns a string for the index page"""

    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Router for page /hbnb"""

    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    """Replaces a string variable"""

    var = text.replace("_", " ")
    return "C %s" % var


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythoniscool(text):
    """Route for the /python path with variable"""

    var = text.replace("_", " ")
    return "Python %s" % var


if __name__ == "__main__":
    app.run(host="0.0.0.0")
