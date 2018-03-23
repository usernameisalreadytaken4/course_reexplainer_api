from flask_restful import Resource


class UserRegisterREST(Resource):

    def put(self, username, user_mail, pwd_hash):
        return {}


class UserAuthorizationREST(Resource):

    def put(self, username, pwd_hash):
        return {}


class UserREST(Resource):

    def get(self, username):
        return {'user': username}
