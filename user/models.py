from django.contrib.auth.admin import User
from django.db import models

GENDER = [
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
]


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(choices=GENDER, max_length=7)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
