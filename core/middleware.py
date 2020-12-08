import time
import datetime
import requests
from django.conf import settings

def timing(get_response):
    def middleware(request):
        request.current_time = datetime.datetime.now()
        t1 = time.time()
        response = get_response(request)
        t2 = time.time()
        print("TOTAL TIME:", (t2 - t1))
        return response

    return middleware


# def token_check(get_response):
#     def middleware(request):
#         if settings.MYAPI_CORE_AUTH_TOKEN == request.headers.get('Authorization'):
#             token = True
#
#         response = get_response(request)
#
#         return response
#
#     return middleware
