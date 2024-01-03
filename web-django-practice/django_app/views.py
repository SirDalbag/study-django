from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product


# Create your views here.
def home(request):
    return render(request, "home.html", context={})


def delivery(request):
    selected_page = request.GET.get(key="page", default=1)
    products = Product.objects.all()
    page_objs = Paginator(object_list=products, per_page=10)
    page_obj = page_objs.page(number=selected_page)
    return render(request, "delivery.html", context={"page_obj": page_obj})
