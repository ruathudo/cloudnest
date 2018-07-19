from flask import Blueprint
from app import docs


api = Blueprint('api', __name__, url_prefix='/api')
from . import user


def register_docs():
    docs.register(user.get_user, blueprint="api")