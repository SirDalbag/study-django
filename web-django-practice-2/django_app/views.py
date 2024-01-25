from django.shortcuts import render, redirect
from django_app import models
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.paginator import Paginator


def pagination(request, objs):
    selected_page = request.GET.get(key="page", default=1)
    page_objs = Paginator(object_list=objs, per_page=6)
    page_obj = page_objs.page(number=selected_page)
    return page_obj


# Create your views here.
def home(request):
    categories = models.Category.objects.all()
    return render(request, "home.html", {"categories": categories})


def sign_up(request):
    if request.method == "GET":
        return render(request, "register.html")
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        print(username, password)
        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"error": True})
        user = User.objects.create(username=username, password=make_password(password))
        login(request, user)
        return redirect(reverse("home"))


def sign_in(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is None:
            return render(request, "login.html", {"error": True})
        login(request, user)
        return redirect(reverse("home"))


def log_out(request):
    logout(request)
    return redirect(reverse("home"))


def products(request, slug):
    category = models.Category.objects.get(slug=slug)
    products = models.Product.objects.all().filter(status=True, category=category)
    return render(request, "products.html", {"page_obj": pagination(request, products)})


def likes(request):
    products_with_likes = models.Product.objects.filter(
        rating__author=request.user, rating__is_like=True
    )
    return render(
        request, "products.html", {"page_obj": pagination(request, products_with_likes)}
    )


def product(request, id):
    product = models.Product.objects.get(id=id)
    key = f"viewed_{product.id}"
    if not request.session.get(key, False):
        product.views_count += 1
        product.save()
        request.session[key] = True
    return render(
        request,
        "product.html",
        {
            "product": product,
            "total_rating": product.total_rating(),
            "is_my_rating": product.is_my_rating(user=request.user),
        },
    )


def tags(request, category, tag):
    category = models.Category.objects.get(slug=category)
    tags = models.Tag.objects.get(slug=tag)
    products = models.Product.objects.all().filter(
        status=True, category=category, tags=tags
    )
    return render(request, "products.html", {"page_obj": pagination(request, products)})


def create_product(request):
    if request.method == "GET":
        categories = models.Category.objects.all()
        tags = models.Tag.objects.all()
        return render(
            request,
            "form.html",
            {"categories": categories, "tags": tags, "GET": True},
        )
    else:
        title = request.POST["title"]
        price = request.POST["price"]
        description = request.POST["description"]
        category = models.Category.objects.get(id=request.POST["category"])
        tags = request.POST.getlist("tags")
        try:
            product = models.Product.objects.create(
                title=title,
                price=price,
                description=description,
                category=category,
            )
            for tag in tags:
                product.tags.add(models.Tag.objects.get(id=tag))
            return render(request, "form.html", {"status": True})
        except Exception as error:
            print(error)
            return render(request, "form.html", {"status": False})


def rating(request, id: str, like: str):
    author = request.user
    product = models.Product.objects.get(id=id)
    is_like = True if like == "1" else False
    try:
        like_obj = models.Rating.objects.get(author=author, product=product)
        if like_obj.is_like and is_like:
            like_obj.delete()
        elif not like_obj.is_like and not is_like:
            like_obj.delete()
        else:
            like_obj.is_like = is_like
            like_obj.save()
    except Exception as _:
        like_obj = models.Rating.objects.create(
            author=author, product=product, is_like=is_like
        )
    return redirect(reverse("product", args=(id,)))


def favorites(request):
    _favorites = models.Favorite.objects.filter(user=request.user)
    return render(
        request,
        "favorites.html",
        {"page_obj": pagination(request, _favorites)},
    )


def favorite(request, id):
    product = models.Product.objects.get(id=id)
    try:
        favorite_product = models.Favorite.objects.get(
            user=request.user, product=product
        )
        favorite_product.delete()
    except Exception:
        favorite_product = models.Favorite.objects.create(
            user=request.user, product=product
        )
    return redirect(reverse("product", args=(id,)))


def search(request):
    search = request.GET.get("search", "")
    products = models.Product.objects.all().filter(status=True, title__icontains=search)
    return render(
        request,
        "products.html",
        {"page_obj": pagination(request, products), "search": search},
    )
