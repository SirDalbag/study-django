from django.contrib import admin
from django_app import models

admin.site.register(models.Book)
admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.Token)
admin.site.register(models.Log)
