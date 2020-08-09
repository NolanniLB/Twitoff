'''SQLAlchemy models for Twitoff'''
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    follower_count = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(280))
    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='tweet', lazy=True)

    def __repr__(self):
        return '<Tweet %r>' % self.text