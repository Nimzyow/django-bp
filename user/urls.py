from django.urls import path

from user import views

# from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path("users/", views.UserListCreate.as_view(), name="user-list-create"),
]
