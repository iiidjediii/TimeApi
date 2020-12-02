from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils import check_time


class TimeCheckView(APIView):
    def get(self, request):
        if settings.MYAPI_CORE_AUTH_TOKEN != request.headers.get('Authorization'):
            raise AuthenticationFailed

        time = request.query_params.get('value')
        
        result = check_time(time)

        response = {'ok': bool(result)}

        return Response(response)
