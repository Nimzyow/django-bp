from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import TimeStamp

GENDER = [
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
]


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    use_in_migrations = True

    def create_user(self, email: str, password=None, **extra_fields) -> AbstractUser:
        """Create a new user profile"""
        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email: str, password: str, **extra_fields) -> AbstractUser:
        """Create a new superuser profile"""
        user = self.create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True

        user.save()

        return user


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserProfileManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"


# Create your models here.
class Profile(TimeStamp):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(choices=GENDER, max_length=7)

    def __str__(self):
        return f"{self.user.first_name.title()} {self.user.last_name.title()}"
