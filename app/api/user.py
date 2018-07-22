from app.models import User
from webargs import fields
from app.schemas import UserSchema
from flask_rest_api import Blueprint
from app.core.utils import InvalidUsage


api = Blueprint('User', __name__, url_prefix='/api/users')


@api.route('/<int:id>', methods=['GET'])
@api.arguments(UserSchema, location='query')
@api.response(UserSchema)
def get_user(args, id):
    print(args)
    user = User.query.get(id)
    if not user:
        raise InvalidUsage('User not found', 404)

    return user

