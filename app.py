import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from resources.user import UserREST, UserRegisterREST, UserAuthorizationREST

from models.user import User
from models.regex import Regex


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{urlencode(os.path.abspath(os.path.basename("course.sqlite")))}'

api = Api(app)
db = SQLAlchemy(app)

api.add_resource(UserREST, '/users/<string:username>')

if __name__ == '__main__':
    app.run(debug=True)
