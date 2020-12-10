import base64

from .models import User


def user_exists(username, password):
    return User.objects.get(user_name=username, password=password)


def is_token_valid(token):
    result = False
    if token is None:
        return result

    try:
        base64_token = token.encode('ascii')
        bytes_token = base64.b64decode(base64_token)
        username, password = bytes_token.decode('ascii').split(':')

        if user_exists(username, password):
            result = True
    except BaseException as exc:
        print(exc)

    return result

# def check_token(request):
#     if request.headers.get('Authorization') is None:
#         raise AuthenticationFailed('Incorrect authentication credentials. Token is not in the header')
#     try:
#         encoded_userpass = request.headers.get('Authorization')
#         base64_bytes = encoded_userpass.encode('ascii')
#         message_bytes = base64.b64decode(base64_bytes)
#         username, password = message_bytes.decode('ascii').split(':')
#     except:
#         raise AuthenticationFailed('Incorrect authentication credentials. Token is not decoded')
#     if User.objects.filter(user_name=username).filter(password=password):
#         return (username, password)
#     else:
#         raise AuthenticationFailed('Incorrect authentication credentials. Invalid token')
#
