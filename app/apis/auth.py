from flask_restplus import Namespace, Resource, fields
from app.models import User

api = Namespace('auth')


@api.route('/login')
class Login(Resource):

    def post(self):
        """User authentication"""
        return {"success": True}