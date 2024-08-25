import json
from datetime import timedelta

from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from sleep.models import Sleep
from user.factories.factories import ProfileFactory
from user.models import Profile


# Create your tests here.
class SleepCreate(TestCase):
    def test_can_save_a_sleep_POST_request(self):
        ProfileFactory.create_batch(1)
        user = User.objects.first()

        payload = {
            "slept_at": (timezone.now() - timedelta(days=1)).isoformat(),
            "sleep_length": 7.5,
        }

        self.client.login(username=user.username, password="password123")
        response = self.client.post(
            "/sleep/sleeps/", data=json.dumps(payload), content_type="application/json"
        )

        self.assertEqual(response.status_code, 201)

        sleep = Sleep.objects.get(profile=user.profile)

        self.assertEqual(sleep.sleep_length, 7.5)
