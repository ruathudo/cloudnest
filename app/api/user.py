from flask_rest_api import Blueprint
from werkzeug.security import generate_password_hash
from flask_jwt_simple import create_jwt
from app import db
from app.models import User
from app.schemas import UserSchema, UserExtSchema
from app.core.utils import AppException
from app.core.auth import check_user_exist
from app.api import PREFIX_VERSION

import logging

# create api blueprint
api = Blueprint('User', __name__, url_prefix=PREFIX_VERSION + '/users')


@api.route('/<int:id>', methods=['GET'])
@api.response(UserSchema)
def get_user(id):
    user = User.query.get(id)
    if not user:
        raise AppException('User Not Found', 404)

    return user


@api.route('/', methods=['POST'])
@api.arguments(UserSchema)
@api.response(UserExtSchema)
def create_user(args):
    user = check_user_exist(username=args.username, email=args.email)

    if user:
        raise AppException('User Already Exist', 409)

    # args auto create user schema
    user = args
    # generate password hash
    user.password = generate_password_hash(args.password)
    # generate token
    token = create_jwt(identity={'id': user.id})

    try:
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)
    except Exception:
        db.session.rollback()
        logging.exception('CANT_SAVE_USER')
        raise AppException('Cannot Save', 500)

    return {'token': token, 'user': user}


@api.route('/<int:id>', methods=['PUT'])
@api.arguments(UserSchema(only=['first_name', 'last_name']))
@api.response(UserSchema)
def update_user(id):
    user = User.query.get(id)

    if not user:
        raise AppException('User Not Found', 404)

    return user
