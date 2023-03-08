from rest_framework.serializers import ModelSerializer
from .models import User

class PrivateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "password",
            "is_superuser",
            "memberId",
        )

# 프로필 관련 serializer
class OneUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "password",
            "isInstructor",
            "first_name",
            "last_name",
            "groups",
            "gender",
            "user_permissions",
            "is_staff",
            "is_active",
            "last_login",
            "is_superuser",
        ]


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
