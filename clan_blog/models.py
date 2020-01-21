""" DB Schema """
from . import db


class User(db.Model):
    """ Model for users """

    id = db.Column(db.Integer,
                   primary_key=True)

    username = db.Column(db.String(50),
                         index=False,
                         unique=True,
                         nullable=False)

    email = db.Column(db.String(50),
                      index=True,
                      unique=True,
                      nullable=False)

    # Add the rest of the model
