from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
    AbstractUser,
)
from common.models import CommonModel
from cart.models import numCart

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


class Activite(CommonModel):
    loginDate = models.DateTimeField(auto_now=True)
    lectureDate = models.DateTimeField(auto_now=True)
    paymentDate = models.DateTimeField(auto_now=True)
    isWithdrawn = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    Withdrawn_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    def create_user(self, username, password, **kwargs):
        if not username:
            raise ValueError("Users must have an email address")
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username=None, password=None, **extra_fields):
        superuser = self.create_user(
            username=username,
            password=password,
        )

        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True

        superuser.save(using=self._db)
        return superuser


class User(AbstractBaseUser, Activite, PermissionsMixin):

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

    username = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        unique=True,
    )

    password = models.CharField(
        max_length=100,
    )
    # pk 대신 사용
    # memberId = models.AutoField(primary_key=True)

    # profile

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
    email = models.CharField(
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

    profileImg = models.URLField(
        max_length=50,
        null=True,
        blank=True,
    )

    # permission 영역

    isInstructor = models.BooleanField(
        default=False,
        null=True,
        blank=True,
    )

    # 구매강의 영역
    ledetaile = models.ManyToManyField(
        "ledetailes.LeDetaile",
        related_name="user",
        null=True,
        blank=True,
    )

    # 제외 영역
    first_name = models.CharField(
        max_length=20,
        editable=False,
    )

    last_name = models.CharField(
        max_length=20,
        editable=False,
    )

    # 강사 영역
    instructorField = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )
    instructorAbout = models.TextField(
        max_length=500,
        blank=True,
        default="",
    )
    instructorCareer = models.TextField(
        max_length=50,
        blank=True,
        default="",
    )

    is_staff = models.BooleanField(
        ("staff status"),
        default=True,
        help_text=("Designates whether the user can log into this admin site."),
    )

    # 헬퍼 클래스 사용
    objects = UserManager()

    # 사용자의 username field는 email으로 설정 (이메일로 로그인)
    USERNAME_FIELD = "username"

    def save(self, *args, **kwargs):
        created = self.pk is None  # Check if the user is being created or updated
        super().save(*args, **kwargs)
        if created:
            numCart.objects.create(user=self)
