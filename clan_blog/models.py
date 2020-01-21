""" DB Schema """
from . import db
from datetime import datetime


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

    admin = db.Column(db.Boolean,
                      nullable=False)

class Posts(db.Model):
    """ Model for posts by users """

    id = db.Column(db.Integer,
                   primary_key=True)

    post = db.Column(db.Text,
                     nullable=False,
                     unique=False,
                     index=False)

    date_created = db.Column(db.DateTime,
                             nullable=False,
                             default=datetime.utcnow)

    user_id = db.Column(db.Integer,
                        db.ForeignKey('user.id'),
                        nullable=False)

    user = db.relationship('User',
                           backref='author', lazy=True)
