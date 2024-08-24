from django.urls import path

from sleep import views

urlpatterns = [
    path("sleeps/", views.SleepListCreate.as_view(), name="sleep-list-create")
]
