from rest_framework import serializers
from .models import Lecture


class LectureListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = (
            "lectureTitle",
            "lectureDifficulty",
            "targetAudience",
            "thumbnail",
        )
