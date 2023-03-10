from rest_framework import serializers
from .models import Lecture, calculatedLecture
from videos.serializers import VideoSerializer

from users.serializers import UserSignUpSerializer, OneUserSerializer
from categories.serializers import CategorySerializer


class LectureSerializer(serializers.ModelSerializer):
    instructor = OneUserSerializer()
    categories = CategorySerializer()


    class Meta:
        model = Lecture
        fields = (
            "lectureTitle",
            "lectureDifficulty",
            "lectureDescription",
            "lectureDifficulty",
            "targetAudience",
            "lectureFee",
            "thumbnail",
            "isOpened",
            "grade",
            "instructor",
            "categories",
        )
        depth = 1


class LectureDetailSerializer(serializers.ModelSerializer):
    lecture = LectureSerializer(read_only=True)
    # totalVideoLength = serializers.SerializerMethodField()
    # video = VideoSerializer()

    class Meta:
        model = calculatedLecture
        fields = "__all__"

    # def get_totalVideoLength(self, obj):
    #     video_lengths = [video.length for video in obj.videos.all()]
    #     print(video_lengths)
    #     total_length = sum(video_lengths)
    #     total_length_in_seconds = total_length.total_seconds()

    #     return total_length_in_seconds
