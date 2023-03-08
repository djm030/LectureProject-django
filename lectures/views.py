from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, exceptions
from .serializers import LectureListSerializer
from .models import Lecture


class LectureList(APIView):
    def get(self, request):
        lectures = Lecture.objects.all()
        serializer = LectureListSerializer(lectures, many=True)
        return Response(serializer.data)
