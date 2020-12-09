from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import check_time
from .services import CheckToken
from rest_framework.exceptions import ValidationError


class TimeCheckView(APIView):
    def get(self, request):
        print(CheckToken(request)) # check authentication
        time = request.query_params.get('value')
        print('value_views', time)
        if time is None:
            raise ValidationError('parameter time not passed')
        result = check_time(time)
        response = {
            'time': bool(result),
            'request time': request.current_time,
            'request.headers.get(Authorization)': request.headers.get('Authorization'),

        }

        return Response(response)
