from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError

from .utils import check_time


class TimeCheckView(APIView):
    def get(self, request):
        time = request.query_params.get('value')
        if time is None:
            raise ValidationError('parameter time not passed')
        result = check_time(time)
        response = {
            'time': bool(result),
        }

        return Response(response)

    def post(self, request):
        time = request.POST.get("value")
        if time is None:
            raise ValidationError('parameter time not passed')
        result = check_time(time)
        response = {
            'time': bool(result),
        }

        return Response(response)