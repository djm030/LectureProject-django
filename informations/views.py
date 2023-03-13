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
        information = Information.objects.all()
        serializer = serializers.InformationSerializer(information)
        return Response(serializer.data)
