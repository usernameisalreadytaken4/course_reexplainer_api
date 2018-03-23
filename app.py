import os
from urllib.parse import urlencode

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from resources.user import UserREST, UserRegisterREST, UserAuthorizationREST


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{urlencode(os.path.abspath(os.path.basename("course.sqlite")))}'

api = Api(app)
db = SQLAlchemy(app)


from models.user import User
from models.regex import Regex


api.add_resource(UserREST, '/users/<string:username>')

if __name__ == '__main__':
    app.run(debug=True)
