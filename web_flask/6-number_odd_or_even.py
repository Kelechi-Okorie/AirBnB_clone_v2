#!/usr/bin/python3
"""A script that starts a Flask web application"""

from flask import Flask
from flask import render_template

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


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """route for /number. displays n only if n is an integer"""

    if type(n) is int:
        return "%i is a number" % n


@app.route("/number_template/<int:n>", strict_slashes=False)
def numbertemplate(n):
    """Returns a template for task 4"""

    if type(n) is int:
        return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """Returns a template that shows whether number is odd or even"""

    if type(n) is int:
        return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
