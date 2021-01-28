from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from flask_babel import Babel

APP = Flask(__name__, static_folder='static')
APP.config['SECRET_KEY'] = 'assembler2021'
# APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.DB'
# APP.config['IMAGES_DIR'] = '/static/images'
# APP.config['ALLOWED_EXTENSIONS'] = {'.png', '.jpg', '.jpeg', '.gif'}

Bootstrap(APP)
# db = SQLAlchemy(APP)
# LOGIN_MANAGER = LoginManager()
# LOGIN_MANAGER.init_app(APP)
# LOGIN_MANAGER.login_view = 'login'

from app import views