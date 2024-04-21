#!/usr/bin/python3
"""
web application on the 0.0.0.0 at port 5000
use storage to fetching data from the storage engine
after each request you must remove the current SQLAlchemy session
then storage.close()

route(
/states_list:
    H1: States
    UL: list of state DBStorage sorted by name(A->Z)
       <Li> State: <state.id>: 

)
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all()
    return render_template('states_list.html', states=states)

@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")