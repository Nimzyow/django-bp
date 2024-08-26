from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import CustomUser
from .serializers import UserSerializer


# Create your views here.
class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    # You normlly don't need below but apply the business logic of filtering here because we dont want
    # super user or staff to get listed in the return
    def get_queryset(self) -> CustomUser:
        return CustomUser.objects.filter(is_staff=False, is_superuser=False)


class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
