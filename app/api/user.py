from flask_rest_api import Blueprint
from marshmallow import fields
from app import db
from app.models import User
from app.schemas import UserSchema
from app.core.utils import AppException
from app.core.auth import check_user_exist
from app.api import PREFIX_VERSION

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
@api.arguments(UserSchema(exclude=['username', 'avatar']))
@api.response(UserSchema)
def create_user(args):
    user = check_user_exist(username=args.username, email=args.email)

    if user:
        raise AppException('User Already Exist', 409)

    user = args
    db.session.add(user)
    db.session.commit()
    db.session.refresh(user)
    return user
