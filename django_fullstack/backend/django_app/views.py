from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db.models import QuerySet
from django_app import models, serializers
import time


def serialization(model, serializer, **kwargs):
    objects = model.objects.filter(**kwargs) if kwargs else model.objects.all()
    return serializer(
        objects,
        many=isinstance(objects, QuerySet),
    ).data


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
def api(request):
    return Response(data={"message": "OK"})


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
def books(request):
    if request.method == "GET":
        return Response(
            data={
                "message": serialization(
                    model=models.Book, serializer=serializers.BookSerializer
                )
            }
        )


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
def book(request, id):
    if request.method == "GET":
        return Response(
            data={
                "message": serialization(
                    model=models.Book, serializer=serializers.BookSerializer, id=id
                )
            }
        )


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
def books_category(request, slug):
    if request.method == "GET":
        objects = models.Book.objects.filter(categories__slug=slug)
        return Response(
            data={
                "message": serializers.BookSerializer(
                    objects,
                    many=isinstance(objects, QuerySet),
                ).data
            }
        )


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
def book_categories(request):
    if request.method == "GET":
        objects = models.Category.objects.filter(
            id__in=request.query_params.getlist("category", [])
        )
        return Response(
            data={
                "message": serializers.CategorySerializer(
                    objects,
                    many=isinstance(objects, QuerySet),
                ).data
            }
        )


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
def categories(request):
    if request.method == "GET":
        return Response(
            data={
                "message": serialization(
                    model=models.Category, serializer=serializers.CategorySerializer
                )
            }
        )


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
def category(request, identifier):
    if request.method == "GET":
        kwargs = {}
        if identifier.isdigit():
            kwargs["id"] = identifier
        else:
            kwargs["slug"] = identifier

        return Response(
            data={
                "message": serialization(
                    model=models.Category,
                    serializer=serializers.CategorySerializer,
                    **kwargs
                )
            }
        )


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
def tags(request):
    if request.method == "GET":
        return Response(
            data={
                "message": serialization(
                    model=models.Tag, serializer=serializers.TagSerializer
                )
            }
        )


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
def tag(request, identifier):
    if request.method == "GET":
        kwargs = {}
        if identifier.isdigit():
            kwargs["id"] = identifier
        else:
            kwargs["slug"] = identifier

        return Response(
            data={
                "message": serialization(
                    model=models.Tag, serializer=serializers.TagSerializer, **kwargs
                )
            }
        )
