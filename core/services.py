from rest_framework.exceptions import AuthenticationFailed
from .models import User
import base64


def CheckToken(request):
    if request.headers.get('Authorization') is None:
        raise AuthenticationFailed('Incorrect authentication credentials. Token is not in the header')
    try:
        encoded_userpass = request.headers.get('Authorization')
        base64_bytes = encoded_userpass.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        username, password = message_bytes.decode('ascii').split(':')
    except:
        raise AuthenticationFailed('Incorrect authentication credentials. Token is not decoded')
    if User.objects.filter(user_name=username).filter(password=password):
        return (username, password)
    else:
        raise AuthenticationFailed('Incorrect authentication credentials. Invalid token')

