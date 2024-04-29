from django.urls import path
from django_app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("posts/<str:username>", views.home, name="posts"),
    path("post/<int:id>", views.post, name="post"),
    path("comment/<int:id>", views.comment, name="comment"),
    path("sign-up", views.sign_up, name="sign-up"),
    path("sign-in", views.sign_in, name="sign-in"),
    path("logout", views.log_out, name="logout"),
]
