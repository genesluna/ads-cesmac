import requests


def login(user_name: str, password: str) -> bool:
    payload = {"user_name": user_name, "password": password}
    response = requests.post('http://127.0.0.1:5000/login', json=payload)

    if response.status_code == 200:
        return True
    else:
        return False
