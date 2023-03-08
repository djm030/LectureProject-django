from rest_framework import serializers
from .models import Lecture, calculatedLecture
from videos.serializers import VideoSerializer


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
