from rest_framework import serializers
from .models import Lecture, calculatedLecture


class LectureListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = (
            "lectureTitle",
            "lectureDifficulty",
            "targetAudience",
            "thumbnail",
        )


class LectureDetailSerializer(serializers.ModelSerializer):
    lecture = LectureListSerializer(read_only=True)

    class Meta:
        model = calculatedLecture
        fields = "__all__"
