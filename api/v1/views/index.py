#!/usr/bin/python3
""" Index of the route """
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """endpoint that retrieves the number of each objects by type """
    classes = {"Amenity": "amenities", "City": "cities",
               "Place": "places", "Review": "reviews",
               "State": "states", "User": "users"}
    stats_objs = {}
    for cls in classes.keys():
        stats_objs[classes[cls]] = storage.count(cls)

    return jsonify(stats_objs)
