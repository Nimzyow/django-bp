from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from user.models import Profile

from .models import Sleep
from .serializers import SleepSerializer


# Create your views here.
class SleepCreateView(generics.CreateAPIView):
    queryset = Sleep.objects.all()
    serializer_class = SleepSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer: SleepSerializer) -> None:
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(profile=profile)


class SleepDetailView(generics.ListAPIView):
    queryset = Sleep.objects.all()
    serializer_class = SleepSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self) -> list[Sleep]:
        user_id = self.kwargs["user_id"]
        profile = get_object_or_404(Profile, user_id=user_id)

        return Sleep.objects.filter(profile=profile).order_by("-slept_at")[:8]
