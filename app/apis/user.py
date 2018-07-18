from flask_restplus import Namespace, Resource
from webargs import fields
from webargs.flaskparser import use_args
from app.models import User

api = Namespace('users')

user_args = {
    'name': fields.Str(required=True)
}


@api.route('/<int:id>')
class UserSingle(Resource):

    def get(self, id):
        """Get user info"""
        return User.query.filter_by(id=id).all()

    def put(self):
        """Update user info"""
        return 200


@api.route('/')
class UserList(Resource):

    @api.doc(params={'name': 'fullname'})
    @use_args(user_args)
    def post(self, args):
        """Create new user"""
        print(args)
        return 201
