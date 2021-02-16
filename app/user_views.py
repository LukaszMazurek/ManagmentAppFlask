"""
Put your user views here
use user.route('your_url')
"""

import os

from flask import render_template
from flask_login import login_required, current_user
from flask import Blueprint

from app import db
from app.models import User, UserGroup, Post, Group
from app.wtforms import BaseStringField, MakePost


user = Blueprint('user', __name__)


@user.route('/dashboard')
@login_required
def dashboard():
    user = current_user
    groups = UserGroup.query.filter_by(user_id=user.id).all()
    groups_data = []
    for group in groups:
        groups_data.append((Group.query.filter_by(id=group.group_id).first().group_name,
                           group.group_id))
    return render_template('dashboard.html', name=user.username,
                           groups_data=groups_data, user=user)


@user.route('/make_group', methods=['GET', 'POST'])
@login_required
def make_group():
    form = BaseStringField()
    flag = None
    if form.validate_on_submit():
        try:
            name = form.string_field.data
            new_group = Group(group_name=name)
            db.session.add(new_group)
            group_id = Group.query.filter_by(group_name=name).first().id
            new_constraint = UserGroup(user_id=current_user.id,
                                        group_id=group_id)
            db.session.add(new_constraint)
            db.session.commit()
            flag = True
        except BaseException:
            # name is already taken
            flag = False
    return render_template('make_group.html', form=form, flag=flag)


@user.route('/forum/<int:id>', methods=['GET', 'POST'])
@login_required
def forum(id):
    form = MakePost()
    if form.validate_on_submit():
        message = form.message.data
        new_post = Post(group_id=id, post=message, username=current_user.username)
        db.session.add(new_post)
        db.session.commit()
    posts = Post.query.filter_by(group_id=id).all()
    posts.reverse()
    return render_template('forum.html', form=form, posts=posts)


@user.route('/add_user/<int:id>', methods=['GET', 'POST'])
@login_required
def add_user(id):
    form = BaseStringField()
    flag = None
    if form.validate_on_submit():
        try:
            username = form.string_field.data
            user_id = User.query.filter_by(username=username).first().id
            new_constraint = UserGroup(user_id=user_id, group_id=id)
            db.session.add(new_constraint)
            db.session.commit()
            flag = True
        except Exception:
            # user doesn't exist
            flag = False
    return render_template('add_participant.html', form=form, flag=flag)
