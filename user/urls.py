from django.urls import path

from sleep import views as sleep_views
from user import views

urlpatterns = [
    path("users/", views.UserListView.as_view(), name="user-list"),
    path("<int:user_id>/sleeps/", sleep_views.SleepDetailView.as_view(), name="user-sleep"),
]
