"""
Put your views here
use @APP.route('/your_url')
"""

import os

from flask import render_template, redirect, url_for, request
from app.wtforms import LoginForm, RegisterForm

from app import APP


@APP.route('/')
def index():
    return render_template('index.html')


@APP.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        
            
    return render_template('login.html', form=form)


@APP.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html', form=form)
