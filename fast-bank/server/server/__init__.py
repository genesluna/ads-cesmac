from controllers.transactions_controller import Withdraw, Deposit
from controllers.user_controller import User, UsersList
from controllers.login_controller import Login

from server.instance import server

from data.ma import ma
from data.db import db

app = server.app
api = server.api


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(User, '/user/<int:id>')
api.add_resource(UsersList, '/users')
api.add_resource(Login, '/login')
api.add_resource(Withdraw, '/withdraw')
api.add_resource(Deposit, '/deposit')

db.init_app(app)
ma.init_app(app)
