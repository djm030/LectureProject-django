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

    MemberId = models.PositiveBigIntegerField(max_length=200)

    UserId = models.CharField(max_length=20)

    Password = models.CharField(max_length=100)

    Nickname = models.CharField(max_length=30)

    Name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=30)
    DateBirth = models.DateField()

    Gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
    )

    PhoneNumber = models.CharField(max_length=20)

    ProfileImg = models.URLField(max_length=50)
    IsInstructor = models.BooleanField(default=False)

    IsAdmin = models.BooleanField(default=False)

