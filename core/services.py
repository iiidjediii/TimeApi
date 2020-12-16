import base64
from rest_framework.exceptions import ValidationError

from .models import User


def user_exist(username, password):
    return User.objects.filter(user_name=username, password=password).exists()


def is_token_valid(token):
    result = False
    if token is None:
        return result

    try:
        base64_token = token.encode('ascii')
        bytes_token = base64.b64decode(base64_token)
        username, password = bytes_token.decode('ascii').split(':')

        if user_exist(username, password):
            result = True
    except:
        return False

    return result
