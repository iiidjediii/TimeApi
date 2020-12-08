from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import check_time
from .models import User
import base64


class TimeCheckView(APIView):
    def get(self, request):

        l = []
        for user in User.objects.all():
            userpass = (user.user_name + ":" + user.password)
            print('userpass', userpass)
            encoded_u = base64.b64encode(userpass.encode()).decode()
            print('encoded_u', encoded_u)
            l.append(encoded_u)
        if request.headers.get('Authorization') in l:
            time = request.query_params.get('value')
            result = check_time(time)
            response = {
                'time': bool(result),
                'request time': request.current_time,
                'req.h.a.': request.headers.get('Authorization'),
            }

            return Response(response)
        else:
            raise AuthenticationFailed



