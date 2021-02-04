"""
Put your authentication views here
use auth.route('your_url')
Views: login, signup, logout, load_user, index
"""

import os

from flask import render_template, redirect
from app.wtforms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from flask import Blueprint

from app import db, LOGIN_MANAGER
from app.models import User


auth = Blueprint('auth.py', __name__)
LOGIN_MANAGER.login_view = "/login"


@LOGIN_MANAGER.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@auth.route('/')
def index():
    return render_template('index.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    state = None
    if form.validate_on_submit():
        try:
            user = User.query.filter_by(username=form.username.data).first()
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect('user/dashboard')
        except BaseException:
            state = 'bad_data'
    return render_template('login.html', form=form, state=state)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    state = None
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data,
                                                 method='sha256')
        try:
            new_user = User(username=form.username.data,
                            email=form.email.data, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            state = 'good_data'
        except Exception:
            state = 'data_taken'
    return render_template('signup.html', form=form, state=state)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')
