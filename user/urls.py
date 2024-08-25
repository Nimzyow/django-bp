from django.urls import path

from user import views

urlpatterns = [
    path("users/", views.UserListCreate.as_view(), name="user-list-create"),
    path("register/", views.UserCreate.as_view(), name="user-register")
]
