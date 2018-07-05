from flask_restplus import Namespace, Resource, fields
from app.models import User

api = Namespace('users')


@api.route('/<username>')
class UserResource(Resource):

    def get(self, username):
        """Get user info"""
        return User.query.filter_by(username=username).all()
