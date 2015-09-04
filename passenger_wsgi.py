#!/usr/bin/env python

"""
passenger setup
"""

import sys, os
INTERP = os.path.join(os.environ['HOME'], 'bile.managersofcaring.com', 
	'bin', 'python')
if sys.executable != INTERP:
	os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())

from app.views import app as application

"""
from flask import Flask
from flask import render_template
application = Flask(__name__)

@application.route('/')
def index():
	return render_template('index.html')
"""

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
