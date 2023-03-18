from rest_framework import serializers
from .models import Lecture, CalculatedLecture
from videos.serializers import VideoSerializer

from users.serializers import (
    UserSignUpSerializer,
    OneUserSerializer,
    InstructorSerializer,
)
from categories.serializers import CategorySerializer
from reviews.serializers import ReviewSerializer


class LectureSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializer()
    categories = CategorySerializer()
    reviews = ReviewSerializer(many=True)
    reviews_num = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Lecture
        fields = (
            "LectureId",
            "lectureTitle",
            "lectureDifficulty",
            "lectureDescription",
            "targetAudience",
            "lectureFee",
            "thumbnail",
            "isOpened",
            "grade",
            "instructor",
            "categories",
            "reviews",
            "reviews_num",
            "rating",
        )

    def get_reviews_num(self, object):
        return object.reviews.count()

    def get_rating(self, object):
        return object.rating()


class LectureListSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializer()
    categories = CategorySerializer()

    class Meta:
        model = Lecture
        fields = (
            "LectureId",
            "lectureTitle",
            "lectureDifficulty",
            "lectureDescription",
            "targetAudience",
            "lectureFee",
            "thumbnail",
            "isOpened",
            "grade",
            "instructor",
            "categories",
        )


class LectureDetailSerializer(serializers.ModelSerializer):
    lecture = LectureSerializer(read_only=True)

    # totalVideoLength = serializers.SerializerMethodField()
    # video = VideoSerializer()

    class Meta:
        model = CalculatedLecture
        fields = "__all__"

    # def get_totalVideoLength(self, obj):
    #     video_lengths = [video.length for video in obj.videos.all()]
    #     print(video_lengths)
    #     total_length = sum(video_lengths)
    #     total_length_in_seconds = total_length.total_seconds()

    #     return total_length_in_seconds
