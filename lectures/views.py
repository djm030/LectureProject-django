from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from .models import Lecture
from users.models import User
from reviews.models import Review
from . import serializers
from rest_framework import permissions

# 전체 게시글을 불러오는 API


class Lectures(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_lectures = Lecture.objects.all()
        serializer = serializers.LectureSerializer(all_lectures, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.isInstructor:
            serializer = serializers.LectureSerializer(data=request.data)
            if serializer.is_valid():
                lecture = serializer.save()
                serializer = serializers.LectureSerializer(lecture)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            raise ParseError


# 하나의 게시글을 불러오는 API


class LecturesDetail(APIView):
    def get_object(self, pk):
        try:
            return Lecture.objects.get(pk=pk)
        except Lecture.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        lecture = self.get_object(pk)
        serializer = serializers.LectureSerializer(lecture)
        return Response(serializer.data)

    def put(self, request, pk):
        lecture = self.get_object(pk)
        serializer = serializers.LectureSerializer(
            lecture,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_lecture = serializer.save()
            return Response(
                serializers.LectureSerializer(updated_lecture).data,
            )
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        room = self.get_object(pk)
        room.delete()
        return Response(status=HTTP_204_NO_CONTENT)


# 강사이름 기반으로 특정 게시글을 불러오는 API


class InstructorName(APIView):
    def get(self, request, username):
        print("username", username)
        try:
            user = User.objects.get(username=username)

            user_lecture = Lecture.objects.filter(instructor=user)
        except Lecture.DoesNotExist:
            raise NotFound
        serializer = serializers.LectureDetailSerializer(user_lecture, many=True)
        return Response(serializer.data)


# 리뷰 기반으로 특정 게시글을 불러오는 API
