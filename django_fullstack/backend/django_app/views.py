from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db.models import QuerySet
from django_app import models, serializers


def serialization(
    model: models, serializer: serializers, id: int = None, slug: dict = {}
):
    objects = model.objects.all() if not id else model.objects.get(id=id)
    if slug.get("category"):
        objects = objects.filter(categories__slug=slug["category"])
    elif slug.get("tag"):
        objects = objects.filter(tags__slug=slug["tag"])
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
                    model=models.Book, serializer=serializers.BookSerializer, id=int(id)
                )
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
def category(request, slug):
    if request.method == "GET":
        return Response(
            data={
                "message": serialization(
                    model=models.Book,
                    serializer=serializers.BookSerializer,
                    slug={"category": slug},
                )
            }
        )


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
def tag(request, slug):
    if request.method == "GET":
        return Response(
            data={
                "message": serialization(
                    model=models.Book,
                    serializer=serializers.BookSerializer,
                    slug={"tag": slug},
                )
            }
        )
