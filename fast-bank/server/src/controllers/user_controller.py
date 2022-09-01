from flask import request
from flask_restx import Resource, fields

from src.models.user import UserModel
from src.schemas.user import UserSchema
from src.services.auth_service import get_hashed_password
from src.server.instance import server

user_ns = server.user_ns

user_schema = UserSchema()
user_list_schema = UserSchema(many=True)

ITEM_NOT_FOUND = 'User not found.'

item = user_ns.model('User', {
    'name': fields.String(description='Name'),
    'user_name': fields.String(description='Username'),
    'password': fields.String(description='Password'),
    'balance': fields.Float(description='Balance', default=0),
    'balance_credit': fields.Float(description='Creditcard balance', default=0),
    'balance_investment': fields.Float(description='Investment balance', default=0)
})


class User(Resource):

    def get(self, id):
        user_data = UserModel.find_by_id(id)
        if user_data:
            return user_schema.dump(user_data), 200
        else:
            return {'message': ITEM_NOT_FOUND}, 404

    @user_ns.expect(item)
    def put(self, id):
        user_data = UserModel.find_by_id(id)
        user_json = request.get_json()

        user_data.name = user_json['name']
        user_data.user_name = user_json['user_name']
        user_data.password = user_json['password']
        user_data.balance = user_json['balance']
        user_data.balance_credit = user_json['balance_credit']
        user_data.balance_investment = user_json['balance_investment']

        user_data.save_to_db()

        return user_schema.dump(user_data), 200

    def delete(self, id):
        user_data = UserModel.find_by_id(id)
        if user_data:
            user_data.delete_from_db()
            return '', 204
        else:
            return {'message': ITEM_NOT_FOUND}, 404


class UsersList(Resource):

    def get(self):
        return user_list_schema.dump(UserModel.find_all()), 200

    @user_ns.expect(item)
    @user_ns.doc('Create a user')
    def post(self):
        user_json = request.get_json()
        user_json['password'] = get_hashed_password(user_json['password'])
        user_data = user_schema.load(user_json)

        user_data.save_to_db()

        return user_schema.dump(user_data), 201
