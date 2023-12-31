#!/usr/bin/python3
"""Starts a flask web application to serve /states_list"""

from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    """Returns a template for rendering the states lists"""

    states = storage.all('State').values
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(self):
    """removes the current SQLAlchemy Session"""

    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
