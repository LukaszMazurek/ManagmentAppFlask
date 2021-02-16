from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from flask_migrate import Migrate


APP = Flask(__name__, static_folder='static')
APP.config['SECRET_KEY'] = 'assembler2021'
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# APP.config['IMAGES_DIR'] = '/static/images'
# APP.config['ALLOWED_EXTENSIONS'] = {'.png', '.jpg', '.jpeg'}

Bootstrap(APP)
db = SQLAlchemy(APP)
migrate = Migrate(APP, db)
LOGIN_MANAGER = LoginManager()
LOGIN_MANAGER.init_app(APP)
LOGIN_MANAGER.login_view = 'login'

from app import models
from app import auth_views
from app import user_views

APP.register_blueprint(auth_views.auth, url_prefix='/')
APP.register_blueprint(user_views.user, url_prefix='/user')
