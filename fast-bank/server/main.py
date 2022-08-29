from flask import Flask, request
from auth import authenticate
from services.users_service import UsersService

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def Login():
    body = request.get_json()

    if (authenticate(body['user_name'], body['password'])):
        return 'Authentication success.', 200
    else:
        return 'Authentication failure.', 401


@app.route('/withdraw', methods=['POST'])
def withdraw():
    body = request.get_json()
    if UsersService.withdraw(body['id'], body['amount']):
        return 'Amount withdrawn successfully.', 200
    else:
        return 'Withdraw failed.', 400


@app.route('/deposit', methods=['POST'])
def deposit():
    body = request.get_json()
    if UsersService.deposit(body['id'], body['amount']):
        return 'Amount deposited successfully.', 200
    else:
        return 'Deposit failed.', 400


@app.route('/user/<name>', methods=['GET'])
def user_by_name(name):
    user = UsersService.get_user_by_name(name)
    return user, 200


@app.route('/user/id/<id>', methods=['GET'])
def user_by_id(id):
    user = UsersService.get_user_by_id(int(id))
    return user, 200


if __name__ == "__main__":
    app.run(debug=True)
