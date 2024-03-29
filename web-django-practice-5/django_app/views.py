from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum, F
from django_app import models


# Create your views here.
@api_view(http_method_names=["GET"])
def get(request):
    objects = (
        models.Shop.objects.filter(date__range=["2024-03-01", "2024-03-31"])
        .values("shop", "category__category", "date")
        .annotate(total=Sum("count") * F("cost"))
    )
    data = []
    for i in objects:
        data.append(
            {
                "Дата": i["date"],
                "Магазин": i["shop"],
                "Категория": i["category__category"],
                "Сумма": i["total"],
            }
        )
    return Response({"data": data})
