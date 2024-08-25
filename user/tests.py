import json

from django.test import TestCase

from user.models import User


# Create your tests here.
class UserListTest(TestCase):
    def test_user_and_profile_created(self):
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
