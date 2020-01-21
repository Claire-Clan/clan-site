""" Flask config class """
import os

class Config:
    """ Config Vars """
    # SECRET
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # SQLALCHEMY
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATION")

    # DEBUG / DEVELOPMENT
    DEBUG = os.getenv("DEBUG")
