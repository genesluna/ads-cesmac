import imp
import requests
import json


def login(user_name: str, password: str) -> dict:
    payload = {"user_name": user_name, "password": password}
    response = requests.post('http://127.0.0.1:5000/api/login', json=payload)

    if response.status_code == 200:
        user = json.loads(response.text)
        return {'success': True, 'user': user}
    else:
        return {'success': False}
