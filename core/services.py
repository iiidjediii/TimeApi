import base64

from .models import User


def user_exist(username, password):
    return User.objects.filter(user_name=username, password=password).exists()


def extract_base64_token(token, encoding='ascii', separator=':'):
    base64_token = token.encode(encoding)
    bytes_token = base64.b64decode(base64_token)
    return bytes_token.decode(encoding).split(separator)


def is_token_valid(token):
    result = False

    try:
        credentials = extract_base64_token(token)
        result = user_exist(*credentials)
    finally:
        return result
