from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models.functions import ExtractMonth, Coalesce
from django.db.models import Sum, Q, F
from django_app import models
import sqlite3


def execute():
    sql = f"""
    SELECT 
        t1.shop, 
        t1.product,
        t1.total_price AS total_price_1,
        t2.product AS product_2,
        t2.total_price AS total_price_2,
        t1.month
    FROM
        (SELECT 
            shop.shop, 
            product.product,
            SUM(sales.count * sales.price) AS total_price,
            strftime('%m', sales.date) AS month
        FROM django_app_sales AS sales
        JOIN django_app_shop AS shop ON sales.shop_id = shop.id
        JOIN django_app_product AS product ON sales.product_id = product.id
        GROUP BY shop.shop, product.product, month) AS t1
    JOIN
        (SELECT 
            shop.shop, 
            product.product,
            SUM(sales.count * sales.price) AS total_price,
            strftime('%m', sales.date) AS month
        FROM django_app_sales AS sales
        JOIN django_app_shop AS shop ON sales.shop_id = shop.id
        JOIN django_app_product AS product ON sales.product_id = product.id
        GROUP BY shop.shop, product.product, month) AS t2
    ON t1.shop = t2.shop AND t1.month = t2.month AND t1.product < t2.product
    LEFT JOIN
        (SELECT 
            shop.shop, 
            product.product,
            SUM(sales.count * sales.price) AS total_price,
            strftime('%m', sales.date) AS month
        FROM django_app_sales AS sales
        JOIN django_app_shop AS shop ON sales.shop_id = shop.id
        JOIN django_app_product AS product ON sales.product_id = product.id
        GROUP BY shop.shop, product.product, month) AS t3
    ON t2.shop = t3.shop AND t2.month = t3.month AND t2.product < t3.product
    WHERE t3.product IS NULL;
    """
    try:
        with sqlite3.connect("db.sqlite3") as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
    except Exception as error:
        return error


# Create your views here.
@api_view(http_method_names=["GET"])
def get(request):
    if request.GET.get("sql", None):
        sales = execute()
        return Response(sales)
    else:
        sales = (
            models.Sales.objects.annotate(month=ExtractMonth("date"))
            .values("month", "shop__shop", "product__product")
            .annotate(total=F("count") * F("price"))
            .values("month", "shop__shop")
            .annotate(
                **{
                    product.product: Coalesce(
                        Sum("total", filter=Q(product__product=product.product)), 0
                    )
                    for product in models.Product.objects.all()
                }
            )
        )
        return Response(
            [
                {"Месяц": i.pop("month"), "Магазин": i.pop("shop__shop"), **i}
                for i in sales
                if i["month"] == int(request.GET.get("month", 0))
            ]
            if request.GET.get("month", None)
            else [
                {"Месяц": i.pop("month"), "Магазин": i.pop("shop__shop"), **i}
                for i in sales
            ]
        )
