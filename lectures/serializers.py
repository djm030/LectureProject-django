from rest_framework.serializers import ModelSerializer
from .models import Lecture
from users.serializers import UserSignUpSerializer


class LectureSerializer(ModelSerializer):
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
