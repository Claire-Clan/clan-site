from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# Define application and config
app = Flask(__name__)
# Important config variables - DO NOT CHANGE -
app.config['SECRET_KEY'] = 'a44ee500f3e13050c6f7133555cff89c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dev.db'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
# Defaults database handler
db = SQLAlchemy(app)
# Hash with bcrypt
bcrypt = Bcrypt(app)
# Login manager views
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'You must be logged in to do that.'

from htdoc import routes
