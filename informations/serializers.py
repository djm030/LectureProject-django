from rest_framework import serializers
from .models import Information
from users.serializers import User

# from users.serializers import OneUserSerializer


class InformationSerializer(serializers.ModelSerializer):
    # user = OneUserSerializer()

    class Meta:
        model = Information
        fields = "__all__"
