from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("m/", views.members, name="members"),
    path("t/", views.trainer, name="trainer"),
    path("c/", views.courts, name="courts"),
    path("m/details/<int:id>", views.details, name="details"),
]
