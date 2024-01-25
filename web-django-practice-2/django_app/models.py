from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    title = models.CharField(
        verbose_name="Title",
        db_index=True,
        primary_key=False,
        unique=True,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=300,
    )
    slug = models.SlugField(
        verbose_name="Link",
        db_index=True,
        primary_key=False,
        unique=True,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=300,
    )

    class Meta:
        app_label = "django_app"
        ordering = ("id",)
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"Category <{self.id}> {self.title} | {self.slug}"

    def count(self):
        return Product.objects.filter(
            status=True, category=Category.objects.get(id=int(self.id))
        ).count()


class Tag(models.Model):
    title = models.CharField(
        verbose_name="Title",
        db_index=True,
        primary_key=False,
        unique=True,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=300,
    )
    slug = models.SlugField(
        verbose_name="Link",
        db_index=True,
        primary_key=False,
        unique=True,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=300,
    )

    class Meta:
        app_label = "django_app"
        ordering = ("id",)
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return f"Tag <{self.id}> {self.title} | {self.slug}"


class Product(models.Model):
    title = models.CharField(
        verbose_name="Title",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=300,
    )
    description = models.TextField(
        verbose_name="Description",
        db_index=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
    )
    price = models.PositiveIntegerField(
        verbose_name="Price",
        db_index=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
    )
    category = models.ForeignKey(
        verbose_name="Category",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=100,
        to=Category,
        on_delete=models.CASCADE,
    )
    tags = models.ManyToManyField(
        verbose_name="Tags",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        default="",
        max_length=100,
        to=Tag,
    )
    views_count = models.PositiveIntegerField(
        verbose_name="Views Count",
        default=0,
        editable=False,
    )
    status = models.BooleanField(
        verbose_name="Status",
        null=False,
        default=True,
    )

    class Meta:
        app_label = "django_app"
        ordering = ("status", "id")
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return f"Product <{self.id}> {self.title} | {self.category}"

    def total_rating(self):
        product = Product.objects.get(id=self.id)
        ratings = Rating.objects.all().filter(product=product)
        return (
            ratings.filter(is_like=True).count() - ratings.filter(is_like=False).count()
        )

    def is_my_rating(self, user):
        product = Product.objects.get(id=self.id)
        ratings = Rating.objects.all().filter(product=product)
        my_rating = ratings.filter(author=user)
        if len(my_rating) > 0:
            return 1 if my_rating[0].is_like else -1
        else:
            return 0


class Rating(models.Model):
    author = models.ForeignKey(
        verbose_name="Author",
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=100,
        to=User,
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        verbose_name="Product",
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=100,
        to=Product,
        on_delete=models.CASCADE,
    )
    is_like = models.BooleanField(
        verbose_name="Is Like",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default=True,
    )

    class Meta:
        app_label = "django_app"
        ordering = ("-product", "-author")

    def __str__(self):
        return f"Rating <{self.id}> [{self.product.id}] {self.product.title} | {self.is_like}"


class Favorite(models.Model):
    user = models.ForeignKey(
        verbose_name="User",
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=100,
        to=User,
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        verbose_name="Product",
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=100,
        to=Product,
        on_delete=models.CASCADE,
    )
