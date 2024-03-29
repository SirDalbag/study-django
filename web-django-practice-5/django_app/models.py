from django.db import models


# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.category}"


class Shop(models.Model):
    shop = models.CharField(max_length=100)
    date = models.DateField()
    count = models.IntegerField()
    cost = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.shop} - {self.date} - {self.category.category}"
