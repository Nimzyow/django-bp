import random

import factory
from django.utils import timezone

from sleep.models import Sleep
from user.factories import ProfileFactory


class SleepFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Sleep

    profile = factory.SubFactory(ProfileFactory)
    slept_at = factory.LazyFunction(
        lambda: timezone.now() - timezone.timedelta(days=random.randint(1 - 15))
    )
    sleep_length = factory.LazyFunction(lambda: round(random.uniform(4, 9), 2))
