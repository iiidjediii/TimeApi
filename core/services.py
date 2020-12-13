import base64

from .models import User


def get_user(username, password):
    return User.objects.get(user_name=username, password=password)


def is_token_valid(token):
    result = False
    if token is None:
        return result

    try:
        base64_token = token.encode('ascii')
        bytes_token = base64.b64decode(base64_token)
        username, password = bytes_token.decode('ascii').split(':')

        if get_user(username, password):
            result = True
    except BaseException as exc:
        print(exc)

    return result

