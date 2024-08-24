from django.shortcuts import render
from rest_framework import generics

from .models import Sleep
from .serializers import SleepSerializer


# Create your views here.
class SleepList(generics.ListCreateAPIView):
    queryset = Sleep.objects.all()
    serializer_class = SleepSerializer

    def perform_create(self, serializer: SleepSerializer) -> None:
        serializer.save(profile=self.request.user.profile)
