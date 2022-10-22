#!/usr/bin/python3
"""creating an api"""

from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask()
