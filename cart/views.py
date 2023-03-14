from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from .models import Cart
from . import serializers


class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart = Cart.objects.get(user=request.user)
        print(cart)
        serializer = serializers.CartSerializer(cart)
        return Response(serializer.data)

    def put(self, requset):
        user = requset.user
        cart = Cart.objects.get(user=user)

        serializer = serializers.CartSerializer(
            cart,
            data=requset.data,
            partial=True,
        )
        if serializer.is_valid():
            user = serializer.save()
            serializer = serializers.CartSerializer(user)

            return Response(serializer.data)
        else:
            return Response(serializer.errors)
