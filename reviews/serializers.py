from rest_framework.serializers import ModelSerializer
from .models import Review
from users.serializers import OneUserSerializer

class ReviewSerializer(ModelSerializer):
    user = OneUserSerializer()

    class Meta:
        model = Review
        fields = "__all__"