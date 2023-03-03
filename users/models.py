from django.db import models

from django.contrib.auth.models import AbstractUser

# 모델
# UserId VARCHAR
# Password VARCHAR
# Name VARCHAR
# Email VARCHAR
# DateBirth DATE
# Gender VARCHAR
# PhoneNumber VARCHAR
# ProfileImg URL
# IsInstructor BOOLEAN
# IsAdmin BOOLEAN
# Nickname VARCHAR


class User(AbstractUser):

    """User Model Definition"""

    class GenderChoices(models.TextChoices):
        MALE = (
            "male",
            "Male",
        )
        FEMALE = (
            "female",
            "Female",
        )

    memberId = models.PositiveBigIntegerField(max_length=200)

    userId = models.CharField(max_length=20)

    password = models.CharField(max_length=100)

    nickname = models.CharField(max_length=30)

    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    dateBirth = models.DateField()

    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
    )

    phoneNumber = models.CharField(max_length=20)

    profileImg = models.URLField(max_length=50)
    isInstructor = models.BooleanField(default=False)

    isAdmin = models.BooleanField(default=False)