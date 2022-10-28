#!/usr/bin/python3
""" Program that define the root of the main app """

from os import environ
from flask import Flask, jsonify, render_template, make_response
from flask_cors import CORS
from api.v1.views import app_views
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix="/api/v1")
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def close_db(error):
    """calls close() on storage"""
    storage.close()


@app.errorhandler(404)
def error_handler(error):
    """ Error Handler """
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
