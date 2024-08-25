import json

from django.test import TestCase

from user.factories.factories import ProfileFactory
from user.models import User


# Create your tests here.
class UserCreateListTest(TestCase):
    def test_can_save_a_user_and_profile_POST_request(self):
        response = self.client.post(
            "/user/register/",
            data=json.dumps(
                {
                    "first_name": "Karen",
                    "last_name": "Doe",
                    "password": "helloWorlds",
                    "username": "karenDoe",
                    "email": "karendoe@example.com",
                    "profile": {"age": 31, "gender": "Female"},
                }
            ),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)

        user = User.objects.first()

        self.assertEqual(user.first_name, "Karen")

    def test_authenticated_user_can_list_users_and_profile_GET_request(self):
        ProfileFactory.create_batch(2)
        response = self.client.get("/user/users/")

        self.assertEqual(response.status_code, 401)

        user = User.objects.first()
        self.client.login(username=user.username, password="password123")
        response = self.client.get("/user/users/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
