from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from .models import LeDetaile
from users.models import User
from . import serializers
from rest_framework import permissions


class LeDetailView(APIView):
    def get(self, request):
        all_ledetaile = ledetaile.objects.all()
        serializer = serializers.LedetailSerializer(all_ledetaile, many=True)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        serializer = serializers.LedetailSerializer(
            user,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            user = serializer.save()
            serializer = serializers.LedetailSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
