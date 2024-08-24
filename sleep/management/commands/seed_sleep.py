import random

from django.core.management.base import BaseCommand

from sleep.factories.factories import SleepFactory
from user.models import Profile


class Command(BaseCommand):
    help = "Seed Sleep"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding data...")
        self.seed_data()
        self.stdout.write(self.style.SUCCESS("Sleep records successfully seeded"))

    def seed_data(self):
        profiles = Profile.objects.all()

        for profile in profiles:
            SleepFactory.create_batch(random.randint(5, 15), profile=profile)
