from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("grappelli/", include("grappelli.urls")),
    path("admin/", admin.site.urls),
    path("", include("django_app.urls")),
    path("api/", include("rest_framework.urls")),
    path("api/token/", TokenObtainPairView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view()),
    path("api/token/verify/", TokenVerifyView.as_view()),
]
