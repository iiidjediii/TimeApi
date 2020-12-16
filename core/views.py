from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError

from .utils import check_time
import json


class TimeCheckView(APIView):
    def post(self, request):
        try:
            body = json.loads(request.body)
            time = body.get("value")
        except:
            raise ValidationError({"detail": 'JSONDecodeError'})
        if time is None:
            raise ValidationError({"detail": 'parameter time not passed'})
        result = check_time(time)
        response = {
            'time': bool(result)
        }

        return Response(response)
