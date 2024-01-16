from django.urls import path
from django_app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("search/", views.search, name="search"),
    path("sign-up", views.sign_up, name="sign-up"),
    path("sign-in", views.sign_in, name="sign-in"),
    path("logout", views.log_out, name="logout"),
    path("likes/", views.likes, name="likes"),
    path("<slug>/", views.products, name="products"),
    path("products/<id>", views.product, name="product"),
    path("<category>/<tag>", views.tags, name="tags"),
    path("create-product", views.create_product, name="create-product"),
    path("product/<id>/rating/<like>/", views.rating, name="rating"),
]
