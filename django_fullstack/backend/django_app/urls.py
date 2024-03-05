from django.urls import path
from django_app import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("api/", views.api, name="api"),
    path("api/books/", views.books, name="books"),
    path("api/book/<id>/", views.book, name="book"),
    path("api/categories/", views.categories, name="categories"),
    path("api/category/<identifier>/", views.category, name="category"),
    path("api/tags/", views.tags, name="tags"),
    path("api/tag/<identifier>/", views.tag, name="tag"),
    path("api/books/<slug>/", views.books_category, name="books-category"),
    path("api/book-categories/", views.book_categories, name="book-categories"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("api/user/register/", views.register),
    path("api/custom-token/", views.custom_token),
    path("api/custom-token/verify", views.custom_token_verify),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
