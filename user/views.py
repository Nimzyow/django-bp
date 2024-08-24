from django.contrib.auth.admin import User
from django.shortcuts import render
from rest_framework import generics

from .models import Profile
from .serializers import UserSerializer


# Create your views here.
class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
