from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import check_time
from .models import User
import base64
# from .services import is_authenticated

class TimeCheckView(APIView):
    def get(self, request):

        def CheckToken(request):
            if request.headers.get('Authorization') == None:
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

        CheckToken(request)

        time = request.query_params.get('value')
        result = check_time(time)
        response = {
            'time': bool(result),
            'request time': request.current_time,
            'request.headers.get(Authorization)': request.headers.get('Authorization'),

        }

        return Response(response)
