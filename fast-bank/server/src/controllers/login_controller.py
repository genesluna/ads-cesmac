from flask import request
from flask_restx import Resource, fields

from src.models.user import UserModel
from src.schemas.user import UserSchema
from src.services.auth_service import authenticate
from src.server.instance import server

user_ns = server.user_ns

user_schema = UserSchema()

item = user_ns.model('Login', {
    'user_name': fields.String(description='Username'),
    'password': fields.String(description='Password')
})


class Login(Resource):

    @user_ns.expect(item)
    def post(self):
        user_json = request.get_json()
        user_data = UserModel.find_by_user_name(user_json['user_name'])

        if user_data:
            if authenticate(user_json['user_name'], user_json['password'], user_data.password):
                user_data.password = None
                return user_schema.dump(user_data), 200
        return 'Authentication failure.', 401
