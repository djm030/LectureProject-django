from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from .models import Information
from . import serializers
from rest_framework import permissions


class InformationView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = Information.objects.get(user=request.user)
        serializer = serializers.InformationSerializer(user)
        return Response(serializer.data)
