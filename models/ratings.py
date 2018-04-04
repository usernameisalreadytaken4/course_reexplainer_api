from app import db

from models.user import User
from models.regex import Regex


class Ratings(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.ForeignKey(User.id), nullable=False)
    post = db.Column(db.ForeignKey(Regex.id), nullable=False)
    mark = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Ratings {self.id}:{self.mark}>'
