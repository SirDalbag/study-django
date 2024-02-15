from django.urls import path
from django_app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api", views.api, name="api"),
]
