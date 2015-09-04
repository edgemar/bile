#!/usr/bin/env python

"""
init script for app package
"""

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
