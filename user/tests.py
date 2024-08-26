import json

from tests.base import BaseAPITestCase
from user.factories.factories import ProfileFactory
from user.models import User


# Create your tests here.
class UserCreateListTest(BaseAPITestCase):
    def test_can_save_a_user_and_profile_POST_request(self):
        response = self.client.post(
            "/signup/",
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

        user = User.objects.last()

        self.assertEqual(user.first_name, "Karen")

    def test_authenticated_user_can_list_users_and_profile_GET_request(self):
        ProfileFactory.create_batch(2)
        response = self.client.get("/user/users/")

        self.assertEqual(response.status_code, 401)

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.get_access_token()}")
        response = self.client.get("/user/users/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)
