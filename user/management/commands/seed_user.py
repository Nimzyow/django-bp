from django.core.management.base import BaseCommand

from user.factories.factories import ProfileFactory


class Command(BaseCommand):
    help = "Seed the database with user data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding data...")
        self.seed_data()
        self.stdout.write(self.style.SUCCESS("Users successfully seeded"))

    def seed_data(self):
        ProfileFactory.create_batch(10)
