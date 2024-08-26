from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from user.factories.factories import ProfileFactory
from user.models import CustomUser


class BaseAPITestCase(APITestCase):
    def setUp(self):
        profile = ProfileFactory.create()
        self.user: CustomUser = profile.user

    def get_access_token(self):
        refresh = RefreshToken.for_user(self.user)
        return str(refresh.access_token)
