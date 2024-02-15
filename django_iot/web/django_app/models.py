from django.db import models


class Vehicle(models.Model):
    id = models.IntegerField(primary_key=True)
    serial_id = models.IntegerField()
    x = models.IntegerField()
    y = models.IntegerField()
    is_working = models.BooleanField()
    fuel = models.IntegerField()
    speed = models.IntegerField()
    date = models.CharField(max_length=255)
