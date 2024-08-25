import json

from django.test import TestCase

from user.factories.factories import ProfileFactory
from user.models import User


# Create your tests here.
class UserCreateListTest(TestCase):
    def test_can_save_a_user_and_profile_POST_request(self):
        response = self.client.post(
            "/user/users/",
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
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 201)

        user = User.objects.first()

        self.assertEqual(user.first_name, "Karen")

    def test_can_list_a_user_and_profile_GET_request(self):
        ProfileFactory.create_batch(2)
        response = self.client.get("/user/users/")

        self.assertEqual(len(response.data), 2)
