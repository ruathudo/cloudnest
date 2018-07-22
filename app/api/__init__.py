from app import rest
from .user import api as user_api

rest.register_blueprint(user_api)
