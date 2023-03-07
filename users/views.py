from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from . import serializers
from rest_framework import status, exceptions, permissions
from django.contrib.auth import authenticate, login, logout


# 유저 프로필 관련 view
class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = User.objects.get(memberId=request.user.memberId)
        serializer = serializers.OneUserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        serializer = serializers.OneUserSerializer(
            user,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            user = serializer.save()
            serializer = serializers.OneUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


# 비밀번호 변경
class UserPasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        if not old_password or not new_password:
            raise exceptions.ParseError("이전 비밀번호와 새로운 비밀번호가 필요합니다.")
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# 유저 회원가입 관련 view
class UsersView(APIView):
    def post(self, request):
        password = request.data.get("password")
        # password 예외처리는 이곳
        if not password:
            raise exceptions.ParseError("password is required")

        serializer = serializers.OneUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            serializer = serializers.OneUserSerializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


## username 유효성 판단
class UsernameView(APIView):
    def get(self, request, username):
        username = User.objects.filter(username=username)
        if username.exists():
            raise exceptions.ValidationError("이미 존재하는 아이디 입니다.")
        else:
            return Response(status=status.HTTP_200_OK)


## 이메일 인증


# login
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            raise exceptions.ParseError("username or password is required")

        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user:
            login(request, user)
            return Response({"login": "True"})
        else:
            return Response({"login": "False"}, status=400)


# logout
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"logout": "True"})
