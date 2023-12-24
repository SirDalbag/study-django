import time
import json

from django.shortcuts import render
from django.core.cache import caches

RamCache = caches["default"]


def get_cache(
    key: str, query: callable = lambda: any, timeout: int = 10, cache: any = RamCache
) -> any:
    data = cache.get(key)
    if data is None:
        data = query()
        cache.set(key, data, timeout)
    return data


def home(request):
    return render(request, "home.html", context={})


def products(request):
    def compute_data() -> int:
        time.sleep(1.0)
        with open("data.json", "r") as file:
            data = json.load(file)
        return data["products"]

    products = get_cache(key="products", query=compute_data, timeout=10, cache=RamCache)
    return render(request, "products.html", context={"products": products})


def login(request):
    return render(request, "login.html", context={})


def sign_up(request):
    return render(request, "sign-up.html", context={})
