from django.urls import path
from django_app import views

urlpatterns = [path("api/", views.api), path("api/token", views.token)]
