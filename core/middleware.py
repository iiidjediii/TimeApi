from django.http import HttpResponseForbidden

from .services import is_token_valid


def token_check(get_response):
    def middleware(request):
        if not is_token_valid(request.headers.get('Authorization')):
            return HttpResponseForbidden("Authorization error!")

        response = get_response(request)

        return response

    return middleware

# import time
# import datetime
# def timing(get_response):
#     def middleware(request):
#         request.current_time = datetime.datetime.now()
#         t1 = time.time()
#         response = get_response(request)
#         t2 = time.time()
#         print("TOTAL TIME:", (t2 - t1))
#         return response
#
#     return middleware