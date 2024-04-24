from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django_app import models, serializers


# Create your views here.
def index(request):
    posts = models.Post.objects.all()
    return render(request, "index.html", context={"posts": posts})


def post(request):
    text = request.POST.get("text", None)
    if text:
        models.Post.objects.create(user=request.user, text=text)
    return redirect("index")


def comment(request, id):
    post = models.Post.objects.get(id=id)
    text = request.POST.get("text", None)
    if text:
        models.Comment.objects.create(user=request.user, post=post, text=text)
    return redirect("index")


@api_view(http_method_names=["GET", "POST", "PUT", "DELETE"])
@permission_classes([AllowAny])
def api(request, id=None):
    if request.method == "GET":
        return Response(
            data={
                "data": serializers.UserSerializer(
                    User.objects.get(id=id) if id else User.objects.all(),
                    many=False if id else True,
                ).data
            },
            status=200,
        )
    elif request.method == "POST":
        User.objects.create(
            username=request.data["username"],
            password=make_password(request.data["password"]),
            email=request.data["email"],
        )
        return Response(data={"message": "success"}, status=200)
    elif request.method == "PUT":
        user = User.objects.get(id=id)
        user.username = request.data["username"]
        user.email = request.data["email"]
        user.save()
        return Response(data={"message": "success"}, status=200)
    elif request.method == "DELETE":
        User.objects.get(id=id).delete()
        return Response(data={"message": "success"}, status=200)


# {"username":"dalbag", "email":"2@mail.ru", "password":"Alomok616!$"}
