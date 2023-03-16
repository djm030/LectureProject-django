from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
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
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        superuser = self.create_user(
            email=email,
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
    email = models.EmailField(
        max_length=30,
        null=True,
        blank=True,
        unique=True,
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

    # 헬퍼 클래스 사용
    objects = UserManager()

    # 사용자의 username field는 email으로 설정 (이메일로 로그인)
    USERNAME_FIELD = "email"

    def save(self, *args, **kwargs):
        created = self.pk is None  # Check if the user is being created or updated
        super().save(*args, **kwargs)
        if created:
            numCart.objects.create(user=self)
