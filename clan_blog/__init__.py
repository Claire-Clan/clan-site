from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv


# Create Database plugin object
db = SQLAlchemy()


def create_app():
    """ Initialize the application """
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    """ Initialize the SQLALCHEMY database plugin """
    db.init_app(app)

    with app.app_context():
         # Include routes
         from . import routes

         # Finish creating application
         return app
