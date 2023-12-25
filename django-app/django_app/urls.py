from django.urls import path
from django_app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.login, name="login"),
    path("sign-up", views.sign_up, name="sign-up"),
    path("products", views.products, name="products"),
    path("products/<int:pk>/", views.product, name="product"),
    path("products/<int:pk>/edit/", views.edit, name="edit"),
    path("products/<int:pk>/delete/", views.delete, name="delete"),
    path("form", views.add, name="add"),
]
