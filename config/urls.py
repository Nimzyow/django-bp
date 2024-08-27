"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from sleep.views import SleepCreateView, SleepDetailView
from user.views import UserCreateView, UserListView

extra_patterns = [
    path("users/", UserListView.as_view(), name="user-list"),
    path("<int:user_id>/sleeps/", SleepDetailView.as_view(), name="user-sleep"),
    path("sleeps/", SleepCreateView.as_view(), name="sleep-list-create"),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path("user/", include(extra_patterns)),
    path("login/", TokenObtainPairView.as_view(), name='api_token_auth'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("signup/", UserCreateView.as_view(), name="register")
]
