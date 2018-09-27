# pip install flask-sqlalchemy
#
# pip install flask-migrate
# flask db init
#
# from app.models import User
# flask db migrate -d "migrate comment"
# flask db upgrade
#
# flask db downgrade

from datetime import datetime
from flask_login import UserMixin
from hashlib import md5
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    snippets = db.relationship('Snippet', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Snippet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    snippetname = db.Column(db.String(20))
    snippet = db.Column(db.String)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    use_count = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Snippet {}>'.format(self.body)
