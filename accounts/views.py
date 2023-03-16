from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework import viewsets
from .tokens import *
from users.models import User

class AuthViewSet(viewsets.GenericViewSet):
    @action(methods=['POST'], detail=False)
    def signin(self, request):
        username = request.data['username']
        password = request.data['password']

        try:
            user = User.objects.get(
                username=username,
                password=password
            )
			
            # payload에 넣을 값 커스텀 가능
            payload_value = user.id
            payload = {
                "subject": payload_value,
            }

            access_token = generate_token(payload, "access")

            data = {
                "results": {
                    "access_token": access_token
                }
            }

            return Response(data=data, status=status.HTTP_200_OK)

        except User.DoesNotExist:

            data = {
                "results": {
                    "msg": "유저 정보가 올바르지 않습니다.",
                    "code": "E4010"
                }
            }

            return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

        except Exception as e:
            print(e)
            data = {
                "results": {
                    "msg": "정상적인 접근이 아닙니다.",
                    "code": "E5000"
                }
            }

            return Response(data=data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)