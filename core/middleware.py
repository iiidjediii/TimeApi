from django.http import HttpResponseForbidden

from .services import is_token_valid


def token_check(get_response):
    def middleware(request):
        if not is_token_valid(request.headers.get('Authorization')):
            return HttpResponseForbidden("Authorization error!")

        response = get_response(request)

        return response

    return middleware

# from django.http import Http404, HttpResponse
# class Custom404Middleware(object):
#     def process_exception(self, request, exception):
#         if isinstance(exception, Http404):
#             msg = unicode(exception)
#             return HttpResponse(msg, status=404)

