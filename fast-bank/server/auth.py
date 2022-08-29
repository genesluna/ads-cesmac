import bcrypt
from services.users_service import UsersService


def authenticate(username: str, password: str) -> bool:
    users = UsersService.get_users()
    for item in users:
        if item['user_name'] == username:
            if __check_password(password, item['password']):
                return True

    return False


def __get_hashed_password(plain_text_password: str) -> str:
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())


def __check_password(plain_text_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_text_password, hashed_password)
