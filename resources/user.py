from os import urandom
from binascii import hexlify
from hashlib import sha512

from flask_restful import Resource

from models.user import User
from common.util import RedisDict
from app import db


r = RedisDict()


class UserREST(Resource):

    def get(self, username):
        if len(username) > 60:
            return {'error': 'too_long_username'}
        user = User.query.filter_by(username=username).first()
        if user:
            return {'user': username}
        return {'error': 'no_user'}


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
        pwd = sha512(f'{user.password}:{salt}'.encode()).hexdigest()
        if pwd == pwd_hash:
            token = sha512(f'{user.username}:{hexlify(urandom(16)).decode()}'.encode()).hexdigest()
            r[token] = user.username
            r.expire(token, 259200)
            return {'token': token}


class UserTokenAuthorizeREST(Resource):

    def post(self, token):
        if token in r:
            username = r[token]
            token = sha512(f'{username}:{hexlify(urandom(16)).decode()}'.encode()).hexdigest()
            r[token] = username
            r.expire(token, 259200)
            return {'token': token}
        return {'error': 'is_not_authorized'}
