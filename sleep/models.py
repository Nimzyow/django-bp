from django.core.validators import MinValueValidator
from django.db import models

from common.models import TimeStamp
from user.models import Profile


# Create your models here.
class Sleep(TimeStamp):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="sleeps")
    slept_at = models.DateTimeField()
    sleep_length = models.FloatField(validators=[MinValueValidator(0)], max_length=2)

    def __str__(self):
        return f"{self.profile.user.first_name} {self.profile.user.last_name} {self.slept_at}"
