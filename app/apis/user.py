from flask_restplus import Namespace, Resource, fields
from app.models import User

api = Namespace('users')


@api.route('/<id>')
class UserAPI(Resource):

    def get(self, uid):
        """Get user info"""
        return User.query.filter_by(id=uid).all()

