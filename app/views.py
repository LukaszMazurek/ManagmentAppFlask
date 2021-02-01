"""
Put your views here
use @APP.route('/your_url')
"""

import os

from flask import render_template, redirect, url_for
from app.wtforms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

from app import APP, db, LOGIN_MANAGER
from app.models import User


@LOGIN_MANAGER.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@APP.route('/')
def index():
    return render_template('index.html')


@APP.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    state = None
    if form.validate_on_submit():
        try:
            user = User.query.filter_by(username=form.username.data).first()
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
        except Exception:
            state = 'bad_data'
            return render_template('login.html', form=form, state=state)
    return render_template('login.html', form=form, state=state)


@APP.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data,
                                                 method='sha256')
        new_user = User(username=form.username.data,
                        email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return render_template('signup.html', form=form, success=True)
    return render_template('signup.html', form=form, success=False)


@APP.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)


@APP.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
