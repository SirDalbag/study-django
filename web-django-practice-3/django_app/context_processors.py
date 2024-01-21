from django_app import models


def products_count(request):
    return {"products_count": models.Product.objects.count()}
