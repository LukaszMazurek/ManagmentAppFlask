"""
Put your models here.
To create database follow the commands.
Run python shell in managment_app folder
*from app import db
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


class UserGroup(db.Model):
    __tablename__ = 'user_group'
    group_user_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    user = db.relationship('User', foreign_keys=[user_id])
    group = db.relationship('Group', foreign_keys=[group_id])


class Group(db.Model):
    __tablename__ = 'group'
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(16), unique=True, nullable=False)


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    username = username = db.Column(db.String(15), nullable=True)
    creation_time = db.Column(db.DateTime,
                              nullable=False, default=datetime.now())
    post = db.Column(db.Text, nullable=True, default='Default message')
    group = db.relationship('Group', foreign_keys=[group_id])
