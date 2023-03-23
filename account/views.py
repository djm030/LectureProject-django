import jwt
import json
from .models import Account
from .token import account_activation_token
from .text import message
from config.my_settings import EMAIL
from rest_framework.views import APIView
from rest_framework import permissions
from . import serializers
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_str


class SignUpView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Activate(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64.encode("utf-8")))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        try:
            if user is not None and account_activation_token.check_token(user, token):
                user.is_active = True
                user.save()
                return HttpResponse(
                    user.email + "계정이 활성화 되었습니다", status=status.HTTP_200_OK
                )
            else:
                return HttpResponse("만료된 링크입니다", status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(traceback.format_exc())
