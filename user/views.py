from django.contrib.auth.admin import User
from rest_framework import generics

from .serializers import UserSerializer


# Create your views here.
class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
