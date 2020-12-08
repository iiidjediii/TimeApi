
#
# def is_authenticated(token):
#     if not token:
#         return False
#
#     result = False
#     try:
#         base64_bytes = token.encode('ascii')
#         message_bytes = base64.b64decode(base64_bytes)
#         username, password = message_bytes.decode('ascii').split(':')
#
#         if User.objects.filter(user_name=username, password=password):
#             result = True
#     finally:
#         return result
