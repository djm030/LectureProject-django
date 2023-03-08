from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, exceptions
from . import serializers
from .models import Lecture, calculatedLecture


class LectureList(APIView):
    def get(self, request):
        lectures = Lecture.objects.all()
        serializer = serializers.LectureListSerializer(lectures, many=True)
        return Response(serializer.data)


class LectureDetail(APIView):
    def get(self, request, pk):
        lecture = calculatedLecture.objects.get(pk=pk)
        serializer = serializers.LectureDetailSerializer(lecture)
        return Response(serializer.data)
