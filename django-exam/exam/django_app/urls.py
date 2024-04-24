from django.urls import path
from django_app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("post", views.post, name="post"),
    path("comment/<int:id>", views.comment, name="comment"),
    path("api/users", views.api, name="api"),
    path("api/users/<int:id>", views.api, name="api"),
]
