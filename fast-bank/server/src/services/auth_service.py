import bcrypt


def authenticate(username: str, password: str, hashed_password: str) -> bool:
    if __check_password(password, hashed_password):
        return True
    else:
        return False


def get_hashed_password(plain_text_password: str) -> str:
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())


def __check_password(plain_text_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_text_password, hashed_password)
