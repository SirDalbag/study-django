from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models


class Product(models.Model):
    id = models.AutoField(
        db_index=True,
        primary_key=True,
        validators=[
            MinLengthValidator(12),
            MaxLengthValidator(12),
        ],
        unique=True,
        editable=True,
        blank=True,
        null=False,
        default=None,
        verbose_name="ID",
        max_length=12,
    )
    name = models.CharField(
        db_index=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        verbose_name="Name",
        max_length=200,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0.0,
        verbose_name="Price",
    )
    image = models.FileField(upload_to="static/src/products")
    status = models.BooleanField(
        null=False,
        default=True,
        verbose_name="Availability",
    )

    class Meta:
        app_label = "django_app"
        ordering = ("status", "-price")
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        if self.status:
            status = "In stock"
        else:
            status = "Out of stock"
        return f"<Product [{self.id}] {self.name} {self.price} | {status}>"
