#!/usr/bin/env python

"""
form file for login with OpenID
"""

from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
	openid = StringField('openid', validators=[DataRequired()])
	remember_me = BooleanField('remember_me', default=False)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
