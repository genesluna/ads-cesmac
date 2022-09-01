from data.db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    user_name = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    balance = db.Column(db.Float, nullable=False)
    balance_credit = db.Column(db.Float, nullable=False)
    balance_investment = db.Column(db.Float, nullable=False)

    def __init__(self, name, user_name, password, balance, balance_credit, balance_investment) -> None:
        self.name = name
        self.user_name = user_name
        self.password = password
        self.balance = balance
        self.balance_credit = balance_credit
        self.balance_investment = balance_investment

    def __repr__(self) -> str:
        return f'UserModel(id={self.id}, name={self.name}, username={self.user_name}, password={self.password}, balance={self.balance}, balance_credit={self.balance_credit}, balance_investment={self.balance_investment})'

    def json(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'user_name': self.user_name,
            'balance': self.balance,
            'balance_credit': self.balance_credit,
            'balance_investment': self.balance_investment
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_user_name(cls, user_name):
        return cls.query.filter_by(user_name=user_name).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
