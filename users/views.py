import jwt
from rest_framework.views import APIView
from . import serializers
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
)
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.exceptions import ParseError, NotFound
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from .models import User, Activite
from rest_framework import status, exceptions, permissions
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404
from config.settings import SECRET_KEY
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


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
        print(request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            serializer = serializers.OneUserSerializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


## username 유효성 판단
class UsernameView(APIView):
    def get(self, request, username):
        username = User.objects.filter(username=username)

        if username.exists():
            return Response("중복된 아이디 입니다.", status=status.HTTP_200_OK)
        else:
            return Response("사용해도 좋습니다.", status=status.HTTP_200_OK)


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
            print(user)
            return Response(status=status.HTTP_200_OK)
        else:
            raise exceptions.ValidationError("username or password is incorrect")


# logout
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"logout": "True"})


# JWT login
class JWTokenView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            raise exceptions.ParseError()

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user:
            token = jwt.encode(
                {
                    "id": user.memberId,
                    "username": user.username,
                },
                settings.SECRET_KEY,
                algorithm="HS256",
            )
            print(token)
            return Response({"token": token})
        else:
            return exceptions.ValidationError("username or password is incorrect")

    # 강사 update


class AddInstructor(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        all_user = User.objects.all()
        serializer = serializers.InstructorSerializer(all_user, many=True)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        serializer = serializers.InstructorSerializer(
            user,
            data=request.data,
            partial=True,
            # isInstructor =true 보내주기 요청
        )
        if serializer.is_valid():
            user = serializer.save()
            serializer = serializers.InstructorSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ActiviteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = User.objects.get(memberId=request.user.memberId)
        serializer = serializers.ActiviteSerializer(user)
        return Response(serializer.data)


# jwt access refresh 토큰 회원가입 로그인 로그아웃 구현


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # jwt 토큰 접근
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "register successs",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )

            # jwt 토큰 => 쿠키에 저장
            res.set_cookie("access", access_token, httponly=True)
            res.set_cookie("refresh", refresh_token, httponly=True)

            return res
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthAPIView(APIView):
    # 유저 정보 확인
    def get(self, request):
        try:
            # access token을 decode 해서 유저 id 추출 => 유저 식별
            access = request.COOKIES["access"]
            payload = jwt.decode(access, SECRET_KEY, algorithms=["HS256"])
            pk = payload.get("user_id")
            user = get_object_or_404(User, pk=pk)
            serializer = serializers.UserSerializer(instance=user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except jwt.exceptions.ExpiredSignatureError:
            # 토큰 만료 시 토큰 갱신
            data = {"refresh": request.COOKIES.get("refresh", None)}
            serializer = TokenRefreshSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                access = serializer.data.get("access", None)
                refresh = serializer.data.get("refresh", None)
                payload = jwt.decode(access, SECRET_KEY, algorithms=["HS256"])
                pk = payload.get("user_id")
                user = get_object_or_404(User, pk=pk)
                serializer = serializers.UserSerializer(instance=user)
                res = Response(serializer.data, status=status.HTTP_200_OK)
                res.set_cookie("access", access)
                res.set_cookie("refresh", refresh)
                return res
            raise jwt.exceptions.InvalidTokenError

        except jwt.exceptions.InvalidTokenError:
            # 사용 불가능한 토큰일 때
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # 로그인
    def post(self, request):
        # 유저 인증
        user = authenticate(
            email=request.data.get("email"), password=request.data.get("password")
        )
        # 이미 회원가입 된 유저일 때
        if user is not None:
            serializer = serializers.UserSerializer(user)
            # jwt 토큰 접근
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "login success",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            # jwt 토큰 => 쿠키에 저장
            res.set_cookie("access", access_token, httponly=True)
            res.set_cookie("refresh", refresh_token, httponly=True)
            return res
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # 로그아웃
    def delete(self, request):
        # 쿠키에 저장된 토큰 삭제 => 로그아웃 처리
        response = Response(
            {"message": "Logout success"}, status=status.HTTP_202_ACCEPTED
        )
        response.delete_cookie("access")
        response.delete_cookie("refresh")
        return response


# jwt 토근 인증 확인용 뷰셋
# Header - Authorization : Bearer <발급받은토큰>
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
