from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import check_time
from .services import CheckToken

class TimeCheckView(APIView):
    def get(self, request):
        print(CheckToken(request)) # check authentication
        time = request.query_params.get('value')
        print(time)
        result = check_time(time)
        response = {
            'time': bool(result),
            'request time': request.current_time,
            'request.headers.get(Authorization)': request.headers.get('Authorization'),

        }

        return Response(response)
