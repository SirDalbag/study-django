from django.urls import path
from django_app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/", views.api),
    path("api/persons/", views.get_persons),
    path("api/persons/<id>/", views.get_person),
    path("api/categories/", views.get_categories),
    path("api/categories/<id>/", views.get_category),
    path("api/clothes/", views.get_clothes),
    path("api/clothes/<id>/", views.get_cloth),
    path("api/post/", views.post_data),
    path("api/report/", views.get_data),
]
