import json
import random
from datetime import timedelta

from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from sleep.factories.factories import SleepFactory
from sleep.models import Sleep
from user.factories.factories import ProfileFactory


# Create your tests here.
class SleepCreate(APITestCase):

    def get_token(self, user: User) -> str:
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def test_authenticated_user_can_save_a_sleep_POST_request(self):
        ProfileFactory.create_batch(1)
        user = User.objects.first()

        payload = {
            "slept_at": (timezone.now() - timedelta(days=1)).isoformat(),
            "sleep_length": 7.5,
        }

        response = self.client.post(
            "/sleep/sleeps/", data=json.dumps(payload), content_type="application/json"
        )
        self.assertEqual(response.status_code, 401)

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.get_token(user)}")
        response = self.client.post(
            "/sleep/sleeps/", data=json.dumps(payload), content_type="application/json"
        )

        self.assertEqual(response.status_code, 201)

        sleep = Sleep.objects.get(profile=user.profile)

        self.assertEqual(sleep.sleep_length, 7.5)

    def test_authenticated_user_can_view_a_users_sleep_GET_request(self):
        ProfileFactory.create_batch(2)
        users = User.objects.all()

        for user in users:
            SleepFactory.create_batch(random.randint(5, 15), profile=user.profile)

        response = self.client.get(f"/user/{users[0].id}/sleeps/")
        self.assertEqual(response.status_code, 401)

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.get_token(users[0])}")
        response = self.client.get(f"/user/{users[1].id}/sleeps/")

        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.data), len(users[1].profile.sleeps.all()[:8]))
