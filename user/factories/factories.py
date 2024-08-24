import random

import factory
from django.contrib.auth.models import User

from user.models import Profile


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user{n}")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    password = factory.PostGenerationMethodCall("set_password", "password123")


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)
    age = factory.LazyAttribute(lambda _: random.randint(18, 60))
    gender = factory.LazyAttribute(lambda _: random.choice(["Male", "Female", "Other"]))
