"""
Put your user views here
use user.route('your_url')
"""
import os

from flask import render_template
from flask_login import login_required, current_user
from flask import Blueprint

from app import db
from app.models import User, Club, UserGroup, Post
from app.wtforms import MakeGroup


user = Blueprint('user', __name__)


@user.route('/dashboard')
@login_required
def dashboard():
    user = current_user
    groups = UserGroup.query.filter_by(user_id=user.id).all()
    groups_data = []
    for group in groups:
        groups_data.append((Club.query.filter_by(id=group.group_id).first().name, group.group_id))
    return render_template('dashboard.html', name=user.username,
                          groups_data=groups_data, user=user)


@user.route('/make_group', methods=['GET', 'POST'])
@login_required
def make_group():
    form = MakeGroup()
    flag = None
    if form.validate_on_submit():
        try:
            name = form.group_name.data
            new_club = Club(name=name)
            db.session.add(new_club)
            db.session.commit()
            group_id = Club.query.filter_by(name=name).first().id
            new_constraint = UserGroup(user_id=current_user.id,
                                       group_id=group_id)
            db.session.add(new_constraint)
            flag = True
            db.session.commit()
        except BaseException:
            # name is already taken
            flag = False
    return render_template('make_group.html', form=form, flag=flag)


@user.route('/forum/<int:id>')
@login_required
def forum(id):
    return render_template('forum.html')


@user.route('/add_user/<int:id>')
@login_required
def add_user(id):
    user = User.query.get_or_404(id)
    return "Add user " + user.username

