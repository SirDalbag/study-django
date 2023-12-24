from django.urls import path
from django_app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("products", views.products, name="products"),
    path("login", views.login, name="login"),
    path("sign-up", views.sign_up, name="sign-up"),
]
