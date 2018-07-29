from marshmallow import fields, validate
from app import ma, rest
from app.models import User


@rest.definition('User')
class UserSchema(ma.ModelSchema):
    id = fields.Integer(dump_only=True)
    first_name = fields.Str(required=True, validate=validate.Length(max=100, error='INVALID_FIRST_NAME'))
    last_name = fields.Str(required=True, validate=validate.Length(max=100, error='INVALID_LAST_NAME'))
    username = fields.Str(required=True, validate=validate.Length(max=100, error='INVALID_USERNAME'))
    email = fields.Str(required=True, validate=validate.Email(error='INVALID_EMAIL'))
    password = fields.Str(required=True, load_only=True,
                          validate=[validate.Length(min=6, max=30, error='INVALID_PASSWORD')])
    avatar = fields.Str()
    time_created = fields.DateTime(dump_only=True)
    time_updated = fields.DateTime(dump_only=True)

    class Meta:
        model = User
        strict = True
        ordered = True


class UserExtSchema(ma.Schema):
    """
    User schema with extra keys
    """
    token = fields.Str(dump_only=True)
    user = fields.Nested(UserSchema)
