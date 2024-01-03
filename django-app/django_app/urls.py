from django.urls import path
from django_app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("sign-in", views.sign_in, name="sign-in"),
    path("sign-up", views.sign_up, name="sign-up"),
    path("log-out", views.log_out, name="log-out"),
    path("products", views.products, name="products"),
    path("products/<int:pk>/", views.product, name="product"),
    path("products/<int:pk>/edit/", views.edit, name="edit"),
    path("products/<int:pk>/delete/", views.delete, name="delete"),
    path("form", views.add, name="add"),
]
