from flask import request
from flask_restx import Resource, fields

from src.models.user import UserModel
from src.schemas.user import UserSchema
from src.server.instance import server

user_ns = server.user_ns

user_schema = UserSchema()

ITEM_NOT_FOUND = 'User not found.'
BAD_REQUEST = 'Bad request.'

item = user_ns.model('Transaction', {
    'id': fields.Integer(description='User Id'),
    'amount': fields.Float(description='Transaction value'),
    'account': fields.String(description='Account (savings, credit, investment)')
})


class Withdraw(Resource):

    @user_ns.expect(item)
    def post(self):
        transaction_json = request.get_json()
        user_data = UserModel.find_by_id(transaction_json['id'])

        if transaction_json['amount'] <= 0:
            return {'message': BAD_REQUEST}, 400

        if user_data:
            if transaction_json['account'] == 'savings':
                user_data.balance -= transaction_json['amount']
            elif transaction_json['account'] == 'credit':
                user_data.balance_credit += transaction_json['amount']
            elif transaction_json['account'] == 'investment':
                user_data.balance_investment -= transaction_json['amount']
            else:
                return {'message': BAD_REQUEST}, 400
        else:
            return {'message': ITEM_NOT_FOUND}, 404

        user_data.save_to_db()

        return user_schema.dump(user_data), 200


class Deposit(Resource):

    @user_ns.expect(item)
    def post(self):
        transaction_json = request.get_json()
        user_data = UserModel.find_by_id(transaction_json['id'])

        if transaction_json['amount'] <= 0:
            return {'message': BAD_REQUEST}, 400

        if user_data:
            if transaction_json['account'] == 'savings':
                user_data.balance += transaction_json['amount']
            elif transaction_json['account'] == 'credit':
                user_data.balance_credit -= transaction_json['amount']
            elif transaction_json['account'] == 'investment':
                user_data.balance_investment += transaction_json['amount']
            else:
                return {'message': BAD_REQUEST}, 400
        else:
            return {'message': ITEM_NOT_FOUND}, 404

        user_data.save_to_db()

        return user_schema.dump(user_data), 200
