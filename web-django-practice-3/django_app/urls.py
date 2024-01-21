from django.urls import path
from django_app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("search/", views.search, name="search"),
    path("form", views.form, name="form"),
    path("products/p<id>", views.product, name="product"),
    path("products/qr-code/p<id>", views.qr_code, name="qr-code"),
]
