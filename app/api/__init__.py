PREFIX_VERSION = '/api/v1'

from .user import api as user_api


def load_resources(rest):
    rest.register_blueprint(user_api)
