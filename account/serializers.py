from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Account


class AccountSerializer(ModelSerializer):
    pass

    class Meta:
        model = Account

        fields = (
            "pk",
            "username",
            "password",
            "nickname",
            "img_profile",
        )

    def validate_password(self, value):
        if value == self.initial_data.get("password1"):
            return value
        raise ValidationError("(password, password1) 불일치")

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            nickname=validated_data["nickname"],
            # img_profile=validated_data['img_profile'],
        )
        user.is_active = False
        user.save()

        message = render_to_string(
            "user/account_activate_email.html",
            {
                "user": user,
                "domain": "localhost:8000",
                "uid": urlsafe_base64_encode(force_str(user.pk)).decode("utf-8"),
                "token": account_activation_token.make_token(user),
            },
        )

        mail_subject = "test"
        to_email = user.username
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()

        return validated_data
