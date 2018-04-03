import os
from urllib.parse import urlencode

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from resources.user import UserREST, UserRegisterREST, UserAuthorizationREST


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{urlencode(os.path.abspath("course.sqlite"))}'

api = Api(app)
db = SQLAlchemy(app)


api.add_resource(UserREST, '/users/<string:username>')
api.add_resource(UserRegisterREST, '/users/register/')
api.add_resource(UserAuthorizationREST, '/users/authorize/')


if __name__ == '__main__':
    app.run(debug=True)
