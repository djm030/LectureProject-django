from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from .models import Activite
from users.models import User
from . import serializers
from rest_framework import permissions


class Activite2(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        all_activite = Activite.objects.all()
        serializer = serializers.ActiviteSerializer(all_activite, many=True)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        serializer = serializers.ActiviteSerializer(
            user,
            data=request.data,
            partial=True,
            #isInstructor =true 보내주기 요청 
        )
        if serializer.is_valid():
            user = serializer.save()
            serializer = serializers.ActiviteSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
