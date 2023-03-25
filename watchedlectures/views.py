from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, exceptions
from . import serializers
from lectures.models import Lecture, CalculatedLecture
from .models import WatchedLecture
from users.models import User


class WatchedLectureView(APIView):
    def get(self, request, lectureId, num):
        try:
            lecture = Lecture.objects.get(LectureId=lectureId)
            cal_lec = CalculatedLecture.objects.get(lecture=lecture)
            log = WatchedLecture.objects.get(lecture=cal_lec, lecture_num=num)
            serializer = serializers.WatchedLectureSerializer(log)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except (Lecture.DoesNotExist, WatchedLecture.DoesNotExist):
            raise exceptions.NotFound("Lecture not found")

    def put(self, request, lectureId, num):
        try:
            lecture = Lecture.objects.get(LectureId=lectureId)
            cal_lec = CalculatedLecture.objects.get(lecture=lecture)
            user = User.objects.get(memberId=request.user.memberId)
            log = WatchedLecture.objects.get(lecture=cal_lec, lecture_num=num)
        except WatchedLecture.DoesNotExist:
            user = User.objects.get(memberId=request.user.memberId)
            log = WatchedLecture.objects.create(
                user=user, lecture=cal_lec, lecture_num=num
            )

        serializer = serializers.WatchedLectureSerializer(
            log, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
