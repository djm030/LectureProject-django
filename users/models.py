from django.db import models

from django.contrib.auth.models import AbstractUser

# 모델
# UserId VARCHAR
# Password VARCHAR
# Name VARCHAR
# Email VARCHARgi
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

    memberId = models.AutoField(
        primary_key=True,
    )

    userId = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )

    password = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    nickname = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
    email = models.EmailField(
        max_length=30,
        null=True,
        blank=True,
    )
    dateBirth = models.DateField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
        null=True,
        blank=True,
    )

    phoneNumber = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )

    profileImg = models.URLField(
        max_length=50,
        null=True,
        blank=True,
    )
    isInstructor = models.BooleanField(
        default=False,
        null=True,
        blank=True,
    )

    isAdmin = models.BooleanField(
        default=False,
        null=True,
        blank=True,
    )
