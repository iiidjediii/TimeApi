import django
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated



class HelloView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        if request.method != 'GET':
            content = {'error': 'only get requests are supported'}

        else:
            if settings.MYAPI_CORE_AUTH_TOKEN == request.headers['token']:
                content = {
                    'OK': 'True'
                    # 'TOKEN': settings.MYAPI_CORE_AUTH_TOKEN,
                    # 'HTTP_HEADER': request.GET,
                    # 'content_type': request.content_type,
                    # 'content_params': request.content_params,
                    # 'headers': request.headers,

                }
            else:
                content = {
                    'OK': 'False'
                }

        return Response(content)
