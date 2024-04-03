from django.db import models


# Create your models here.
class Shop(models.Model):
    shop = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.shop}"


class Product(models.Model):
    product = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.product}"


class Sales(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()
    price = models.IntegerField()
    date = models.DateField()

    def __str__(self) -> str:
        return f"{self.shop.shop} | {self.product.product} | {self.count} | {self.price} | {self.date}"
