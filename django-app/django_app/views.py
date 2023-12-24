from django.shortcuts import render
import json


def home(request):
    return render(request, "home.html", context={})


def products(request):
    with open("data.json", "r") as file:
        data = json.load(file)
    return render(request, "products.html", context={"products": data["products"]})


def login(request):
    return render(request, "login.html", context={})


def sign_up(request):
    return render(request, "sign-up.html", context={})
