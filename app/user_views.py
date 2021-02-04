"""
Put your user views here
use user.route('your_url')
Views: dashboard
"""
import os

from flask import render_template, redirect
from flask_login import login_required, current_user
from flask import Blueprint

from app import db
from app.models import User


user = Blueprint('user.py', __name__)


@user.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)
