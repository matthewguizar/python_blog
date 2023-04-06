from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQL_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)
Migrate(app, db)


login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'

from myproject.core.views import core
from myproject.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(error_pages)
