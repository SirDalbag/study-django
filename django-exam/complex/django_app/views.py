from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django_app import models


# Create your views here.
@login_required(login_url="sign-up")
def home(request, username=None):
    if request.method == "POST":
        title = request.POST.get("title")
        text = request.POST.get("text")
        if title and text:
            models.Post.objects.create(user=request.user, title=title, text=text)
        return redirect("home")
    if username:
        posts = models.Post.objects.filter(user__username=username)
    else:
        username = request.user.username
        posts = models.Post.objects.all()
    selected_page = request.GET.get(key="page", default=1)
    page_objs = Paginator(object_list=posts, per_page=2)
    page_obj = page_objs.page(number=selected_page)
    return render(
        request, "home.html", context={"page_obj": page_obj, "username": username}
    )


@login_required(login_url="sign-up")
def post(request, id):
    post = models.Post.objects.get(id=id)
    selected_page = request.GET.get(key="page", default=1)
    comments = models.Comment.objects.filter(post=post)
    page_objs = Paginator(object_list=comments, per_page=4)
    page_obj = page_objs.page(number=selected_page)
    return render(request, "post.html", context={"post": post, "page_obj": page_obj})


@login_required(login_url="sign-up")
def comment(request, id):
    post = models.Post.objects.get(id=id)
    if request.method == "POST":
        comment = request.POST.get("comment")
        if comment:
            models.Comment.objects.create(user=request.user, post=post, text=comment)
    return redirect(f"/post/{id}")


def sign_up(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        user = User.objects.create(username=username, password=make_password(password))
        login(request, user)
        return redirect("home")
    return render(request, "sign-up.html")


def sign_in(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("home")
    return render(request, "sign-in.html")


def log_out(request):
    logout(request)
    return redirect("sign-in")
