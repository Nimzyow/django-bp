from django.contrib.auth.admin import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer


# Create your views here.
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    # You normlly don't need below but apply the business logic of filtering here because we dont want
    # super user or staff to get listed in the return
    def get_queryset(self) -> User:
        return User.objects.filter(is_staff=False, is_superuser=False)


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
