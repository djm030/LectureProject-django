from rest_framework import serializers
from .models import Lecture, calculatedLecture
from users.serializers import UserSignUpSerializer


class LectureSerializer(serializers.ModelSerializer):
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
        )


class LectureDetailSerializer(serializers.ModelSerializer):
    lecture = LectureSerializer(read_only=True)

    class Meta:
        model = calculatedLecture
        fields = "__all__"
