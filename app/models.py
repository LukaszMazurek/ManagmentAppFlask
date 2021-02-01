"""
Put your models here.
To create databse follow the commands.
Run python shell in managment_app folder
*from app import database.db
*db.create_all()
*exit()
This will create all your models and put
your database in app folder
"""

from app import db
from app import UserMixin
from datetime import datetime


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=True, nullable=False)
    path = db.Column(db.String(100), nullable=True)


class Group(db.Model):
    __tablename__ = 'group'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=True, nullable=False)
    text = db.Column(db.String(100), unique=True, nullable=False)


class Meeting(db.Model):
    __tablename__ = 'meeting'
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'),
                         nullable=False)
    date_start = db.Column(db.Date, nullable=False)
    date_end = db.Column(db.Date, nullable=False)
    time_start = db.Column(db.Time, nullable=False)
    time_end = db.Column(db.Time, nullable=False)
    place = db.Column(db.String(100), nullable=True)
    group_meeting = db.relationship('Group', foreign_keys=[group_id])


class UserGroup(db.Model):
    __tablename__ = 'user_group'
    user_group_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    user = db.relationship('User', foreign_keys=[user_id])
    group = db.relationship('Group', foreign_keys=[group_id])


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    creation_time = db.Column(db.DateTime,
                              nullable=False, default=datetime.now())
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    post = db.Column(db.Text, nullable=True, default='New message')
