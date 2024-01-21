from django.shortcuts import render
from django_app import models
from django.core.paginator import Paginator
from django.core.files.base import ContentFile
from django.views.decorators.cache import cache_page
from django.http import HttpResponse
from django.urls import reverse
import qrcode
from io import BytesIO


def paginator(request, objs):
    selected_page = request.GET.get(key="page", default=1)
    page_objs = Paginator(object_list=objs, per_page=3)
    page_obj = page_objs.page(number=selected_page)
    return page_obj


@cache_page(10)
def home(request):
    products = models.Product.objects.all().filter(status=True)
    return render(request, "home.html", {"products": paginator(request, products)})


def search(request):
    if request.method == "POST":
        search = request.POST.get("search", "")
        products = models.Product.objects.all().filter(
            status=True, name__icontains=search
        )
        print(search)
        return render(request, "home.html", {"products": paginator(request, products)})


def product(request, id):
    product = models.Product.objects.get(id=id)
    return render(request, "product.html", {"product": product})


def qr_code(request, id):
    product = models.Product.objects.get(id=id)
    if not product.qr_code:
        product_url = request.build_absolute_uri(reverse("product", args=[id]))
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(product_url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img_bytes = BytesIO()
        img.save(img_bytes, format="PNG")
        filename = f"qr_code_{id}.png"
        product.qr_code.save(filename, ContentFile(img_bytes.getvalue()), save=True)
        product.save()
    return render(request, "qr-code.html", {"product": product})


def form(request):
    if request.method == "GET":
        return render(request, "form.html")
    else:
        name = request.POST["name"]
        description = request.POST["description"]
        price = float(request.POST["price"].replace(",", "."))
        image = request.FILES["image"]
        try:
            product = models.Product.objects.create(
                name=name, description=description, price=price, image=image
            )
            status = "success"
        except Exception:
            status = "error"
        return render(request, "form.html", {"status": status})
