from django.urls import path
from django_app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("delivery/", views.delivery, name="delivery"),
]
