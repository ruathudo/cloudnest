from flask import Blueprint
from flask_restplus import Api
from .auth import api as auth_ns
from .user import api as user_ns

blueprint = Blueprint('api', __name__)
api = Api(blueprint, title='Cloud Nest')

api.add_namespace(auth_ns, path='/auth')
api.add_namespace(user_ns, path='/users')
