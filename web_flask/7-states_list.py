#!/usr/bin/python3
'''
    Script that starts a Flask web application.
    Web application must be listening on 0.0.0.0, port 5000
'''

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    all_states = storage.all('State')
    return render_template('/7-states_list.html', states=all_states)

@app.teardown_appcontext
def teardown(exception):
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
