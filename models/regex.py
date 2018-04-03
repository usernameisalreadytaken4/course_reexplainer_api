from datetime import datetime

from app import db

from .user import User


class Regex(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    expression = db.Column(db.Unicode(512), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    author = db.ForeignKey(User.id)

    def __repr__(self):
        return f'<Regex {self.id}:{self.author}>'
