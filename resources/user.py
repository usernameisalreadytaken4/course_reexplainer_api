from hashlib import sha512

from flask_restful import Resource, marshal_with, fields

from models.user import User
from app import db


class UserRegisterREST(Resource):

    def put(self, username, user_mail, pwd_hash):
        if len(username) > 60:
            return {'error': 'too_long_username'}
        if len(user_mail) > 140:
            return {'error': 'too_long_email'}
        user = User(username=username, email=user_mail, password=pwd_hash)
        db.session.add(user)
        db.session.commit()
        return {'status': 'created'}


class UserAuthorizationREST(Resource):

    def post(self, username, pwd_hash, salt):
        if len(username) > 60:
            return {'error': 'no_user'}
        user = User.query.filter_by(username=username).first()
        if not user:
            return {'error': 'no_user'}
        else:
            pwd = sha512(f'{user.password}:{salt}'.encode()).hexdigest()
            if pwd == pwd_hash:
                pass
                # TODO: GENERATE USER TOKENS AND SAVE THEM IN REDIS
        return {}


class UserREST(Resource):

    def get(self, username):
        if len(username) > 60:
            return {'error': 'too_long_username'}
        user = User.query.filter_by(username=username).first()
        if user:
            return {'user': username}
        else:
            return {'error': 'no_user'}
