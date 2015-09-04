#!/usr/bin/env python

"""
the view function, views.py
"""
from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Kelsey'}  # fake rando
    posts = [ # posts, "as if!!!", i.e. fake
    {
    'author': {'nickname': 'Lou'},
    'body': 'Went to the Apollo, shoulda seen em go go go.'
    },
    {
    'author': {'nickname': 'Pat'},
    'body': 'Yer a real tough cookie with a long history.'
    }
    ]
    return render_template('index.html', 
        title='bile Home',
        user=user,
        posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
            (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
        title='Sign In',
        form=form)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
