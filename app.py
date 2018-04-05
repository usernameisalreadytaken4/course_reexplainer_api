from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from config import config


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///course.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = config.SECRET_KEY


api = Api(app)
db = SQLAlchemy(app)


from resources.user import UserREST, UserRegisterREST, UserAuthorizationREST, UserTokenAuthorizeREST


api.add_resource(
    UserREST,
    '/users/?username=<string:username>'
)
api.add_resource(
    UserRegisterREST,
    '/users/register/?username=<string:username>&mail=<string:user_mail>&pwd=<string:pwd_hash>'
)
api.add_resource(
    UserAuthorizationREST,
    '/users/authorize/?username=<string:username>&pwd=<string:pwd_hash>&s=<string:salt>'
)

api.add_resource(
    UserTokenAuthorizeREST,
    '/users/authorize/?token=<string:token>'
)


if __name__ == '__main__':
    app.run(debug=True)
