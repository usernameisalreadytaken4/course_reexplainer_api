# https://flask-restful.readthedocs.io/en/latest/intermediate-usage.html#project-structure

from resources.ratings import RatingsREST
from resources.user import UserREST, UserRegisterREST, UserAuthorizationREST, UserTokenAuthorizeREST
from resources.regex import RegexREST