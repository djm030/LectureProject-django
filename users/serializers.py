from rest_framework.serializers import ModelSerializer
from .models import User


# 프로필 관련 serializer
class OneUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "password",
            "groups",
            "user_permissions",
            "last_login",
            "is_superuser",
            "loginDate",
            "lectureDate",
            "paymentDate",
            "isWithdrawn",
            "created_at",
            "Withdrawn_at",
        ]
        depth = 4



# 로그인 관련 serializer
class UserSignUpSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            "nickname",
            "phoneNumber",
            "dateBirth",
            "gender",
        )


# 강사 관련


class InstructorSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "instructorField",
            "instructorAbout",
            "instructorCareer",
        )


# ACTIVITE 관련


class ActiviteSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "ledetaile",
            "loginDate",
            "lectureDate",
            "paymentDate",
            "isWithdrawn",
            "created_at",
            "Withdrawn_at",
        )


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "groups",
            "user_permissions",
            "last_login",
            "is_superuser",
            "loginDate",
            "lectureDate",
            "paymentDate",
            "isWithdrawn",
            "created_at",
            "Withdrawn_at",
        ]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
        )
        return user


class UserNameSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)


class UserLedetaileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "calculatedLecture",
        )
