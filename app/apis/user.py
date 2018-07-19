from app.models import User
from webargs import fields
from app.schemas import UserSchema
from flask_apispec import marshal_with, use_kwargs
from . import api


@api.route('/users/<int:id>', methods=['GET'])
@use_kwargs({'id': fields.Int()})
@marshal_with(UserSchema(), 200)
def get_user(id):
    return User.query.get(id).one()

