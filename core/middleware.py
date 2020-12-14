from django.http import HttpResponseForbidden, JsonResponse

from .services import is_token_valid


def token_check(get_response):
    def middleware(request):
        if not is_token_valid(request.headers.get('Authorization')):
            # return HttpResponseForbidden("Authorization error!")
            return JsonResponse({"detail": "Authorization error!"})
        response = get_response(request)

        return response

    return middleware


class CustomExcMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before the view (and later middleware) are called.
        response = self.get_response(request)
        # Code to be executed for each request before the view (and later middleware.
        return response

    def process_exception(self, request, exception):
        try:
            if isinstance(exception, Exception):
                return JsonResponse({"Error": exception.__module__}, status=500)
        except:
            return JsonResponse({"detail":"something unexpected"})