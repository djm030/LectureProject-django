from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Cart
from . import serializers


class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart = Cart.objects.all()
        serializer = serializers.CartSerializer(cart)
        return Response(serializer.data)

    # 로그인 회원만 접근/

    # def put(self, request):
    #     pass

    # 결제가 되면 장바구니에서 삭제
