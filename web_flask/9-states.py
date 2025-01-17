#!/usr/bin/python3
'''
    Script that starts a Flask web application.
    Web application must be listening on 0.0.0.0, port 5000
'''

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_show(id):
    if "State.{}".format(id) in storage.all(State):
        state = storage.all(State)["State.{}".format(id)]
    else:
        state = None
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown(ext):
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
