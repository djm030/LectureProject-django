from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, exceptions
from . import serializers
from .models import Video


class VideoList(APIView):
    def get(self, request):
        videos = Video.objects.all()
        serializer = serializers.VideoSerializer(videos, many=True)
        return Response(serializer.data)


class oneVideo(APIView):
    def get_object(self, pk):
        try:
            return Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        video = self.get_object(pk)
        serializer = serializers.VideoSerializer(video)
        return Response(serializer.data)
