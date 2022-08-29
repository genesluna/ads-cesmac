import requests
import json


def get_user(user_name):
    response = requests.get('http://127.0.0.1:5000/user/' + user_name)
    user = json.loads(response.text)

    return user


def get_user_by_id(user_id):
    response = requests.get('http://127.0.0.1:5000/user/id/' + user_id)
    user = json.loads(response.text)

    return user


def deposit(user_id, amount):
    payload = {"id": user_id, "amount": amount}
    response = requests.post('http://127.0.0.1:5000/deposit', json=payload)

    if response.status_code == 200:
        return True
    else:
        return False


def withdraw(user_id, amount):
    payload = {"id": user_id, "amount": amount}
    response = requests.post('http://127.0.0.1:5000/withdraw', json=payload)

    if response.status_code == 200:
        return True
    else:
        return False
