from django.urls import path
from django_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("api/", views.api, name="api"),
    path("api/books/", views.books, name="books"),
    path("api/book/<int:id>/", views.book, name="book"),
    path("api/categories/", views.categories, name="categories"),
    path("api/category/<str:slug>/", views.category, name="category"),
    path("api/tag/<str:slug>/", views.tag, name="tag"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
