from django.contrib import admin
from django_app import models

# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.Product)
admin.site.register(models.Rating)
admin.site.register(models.Favorite)
