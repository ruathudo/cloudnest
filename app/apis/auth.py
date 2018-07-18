from flask_restplus import Namespace, Resource, fields
from app.models import User

api = Namespace('auth')


@api.route('/')
class Auth(Resource):

    def post(self):
        """User Login"""
        return {"success": True}

    def delete(self):
        """User logout"""
        return {"success": True}


@api.route('/reset')
class ResetPassword(Resource):

    def post(self):
        """Send forget password email"""
        return {"success": True}

    def get(self):
        """Reset password"""
        return {"success": True}
