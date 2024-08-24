from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from user.models import Profile

from .models import Sleep
from .serializers import SleepSerializer


# Create your views here.
class SleepListCreate(generics.CreateAPIView):
    queryset = Sleep.objects.all()
    serializer_class = SleepSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer: SleepSerializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(profile=profile)
