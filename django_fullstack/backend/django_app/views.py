from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.db.models import QuerySet
from django_app import models, serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django_app import utils


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


@api_view(http_method_names=["POST"])
@permission_classes([AllowAny])
def register(request) -> Response:
    print("request.data: ", request.data)

    username = request.data.get("username", None)
    password = request.data.get("password", None)
    if username and password:
        User.objects.create(username=username, password=make_password(password))
        return Response(data={"success": "Account created"}, status=status.HTTP_200_OK)
    else:
        return Response(
            data={"error": "Invalid login or password"},
            status=status.HTTP_401_UNAUTHORIZED,
        )


@api_view(http_method_names=["GET", "POST"])
def custom_token(request):
    if request.method == "GET":
        return Response(data={"message": "OK"})
    elif request.method == "POST":
        try:
            username = request.data["username"]
            password = request.data["password"]
            if username and password:  # and utils.check_password(password)
                user = authenticate(username=username, password=password)
                if user:
                    token, created = models.Token.objects.get_or_create(
                        user=user, defaults={"token": utils.generate_token(password)}
                    )
                return Response(
                    data={"message": {"token": serializers.TokenSerializer(token).data}}
                )
            return Response(data={"message": "Invalid username or password"})
        except Exception as error:
            return Response(data={"message": str(error)})


@api_view(http_method_names=["GET", "POST"])
def custom_token_verify(request):
    if request.method == "GET":
        return Response(data={"message": "OK"})
    elif request.method == "POST":
        try:
            token = request.data["token"]
            if token:
                try:
                    token_obj = models.Token.objects.get(token=token)
                    if token_obj.is_expired:
                        return Response({"message": "Token has expired!"})
                    else:
                        return Response({"message": "Success!"})
                except Exception as error:
                    return Response(data={"message": str(error)})
            return Response(data={"message": "Token is missing!"})
        except Exception as error:
            return Response(data={"message": str(error)})
