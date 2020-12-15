from django.http import JsonResponse

from .services import is_token_valid


def token_check(get_response):
    def middleware(request):
        if not is_token_valid(request.headers.get('Authorization')):
            return JsonResponse({"detail": "Authorization error!"}, status=403)

        response = get_response(request)
        return response
    return middleware


def exception_check(get_response):
    def middleware(request):
        return get_response(request)

    def process_exception(request, exception):
        message = {
            'detail': "Server Error",
            # 'intitle': str(exception),
            # 'module':  exception.__module__,
        }
        return JsonResponse(message, status=500,)

    middleware.process_exception = process_exception

    return middleware

