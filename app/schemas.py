from marshmallow import fields, validate
from app import ma
from app.models import User


class UserSchema(ma.ModelSchema):
    first_name = fields.Str(validate.Length(max=100, error='INVALID_FIRST_NAME'))
    last_name = fields.Str(validate.Length(max=100, error='INVALID_LAST_NAME'))
    username = fields.Str(required=True, validate=validate.Email(error='INVALID_EMAIL'))
    password = fields.Str(required=True, load_only=True,
                          validate=[validate.Length(min=6, max=30, error='INVALID_PASSWORD')])

    class Meta:
        model = User
        exclude = ['password']
