#!/usr/bin/python3
"""Starts a flask web application to serve /states_list"""

from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """Returns a template for rendering the list of states with their cities"""

    states = storage.all('State')
    if id:
        k = "{}.{}".format('State', id)
        if k in states:
            states = states[k]
        else:
            states = None
    else:
        states = states.values()
    return render_template('9-states.html', id=id, states=states)


@app.teardown_appcontext
def teardown(self):
    """removes the current SQLAlchemy Session"""

    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
