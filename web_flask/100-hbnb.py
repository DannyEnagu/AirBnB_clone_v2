#!/usr/bin/python3
"""Define ``10-hbnb_filters`` module. Import Flask
   class and create a new class instance called ``app``.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place


app = Flask('web_flask')


@app.route('/hbnb', strict_slashes=False)
def hbnb_filters():
    """Load all cities of a State
    """
    all_states = storage.all(State)
    all_amenities = storage.all(Amenity)
    all_places = storage.all(Place)
    return render_template('100-hbnb.html',
                           states=all_states,
                           amenities=all_amenities,
                           places=all_places)


@app.teardown_appcontext
def close_db_session(exc):
    """Remove/close the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
