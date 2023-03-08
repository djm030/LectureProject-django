from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from users.models import User


class JWTauthentication(BaseAuthentication):
    def authenticate(self, request):
        print(request.headers)
        return request
