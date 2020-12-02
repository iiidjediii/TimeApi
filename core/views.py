from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView


class TimeCheckView(APIView):
    def get(self, request):
        if settings.MYAPI_CORE_AUTH_TOKEN != request.headers.get('Authorization'):
            raise AuthenticationFailed

        return Response({'ok': True})
