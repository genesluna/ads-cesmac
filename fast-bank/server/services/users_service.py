import json


def open_users():
    with open('users.json', 'r') as f:
        users = json.load(f)
    return users


def write_users(users):
    with open('users.json', 'w') as f:
        users = json.dump(users, f, indent=2)


class UsersService:
    JSON_FILE = 'users.json'

    def get_users() -> dict:
        users = open_users()
        return users['users']

    def get_user_by_name(user_name: str):
        users = open_users()

        for user in users['users']:
            if user['user_name'] == user_name:
                user['password'] = None
                return user
        return None

    def get_user_by_id(user_id: int):
        users = open_users()

        for user in users['users']:
            if user['id'] == user_id:
                user['password'] = None
                return user
        return None

    def withdraw(user_id, amount):
        try:
            users = open_users()

            for user in users['users']:
                if user['id'] == user_id:
                    user['balance'] = user['balance'] - amount

            write_users(users)
        except:
            return False

        return True

    def deposit(user_id, amount):
        try:
            users = open_users()

            for user in users['users']:
                if user['id'] == user_id:
                    user['balance'] = user['balance'] + amount

            write_users(users)

        except:
            return False

        return True
