from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(
        verbose_name="User",
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        max_length=300,
        to=User,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    name = models.CharField(
        verbose_name="Name",
        db_index=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="",
        max_length=300,
    )
    avatar = models.ImageField(
        verbose_name="Avatar",
        validators=[FileExtensionValidator(["jpg", "png", "jpeg"])],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="profile\avatars\default.png",
        upload_to="profile/avatars",
    )

    class Meta:
        app_label = "auth"
        ordering = ("-user",)

    def __str__(self):
        return f"ID [{self.id}] {self.name}"


class Product(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(
        null=True, blank=True, default="Product has no description"
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, blank=False
    )
    image = models.ImageField(
        upload_to="product/img/",
        validators=[FileExtensionValidator(["jpg", "png", "jpeg"])],
        null=False,
        blank=False,
    )
    qr_code = models.ImageField(
        upload_to="product/qr-codes/",
        validators=[FileExtensionValidator(["jpg", "png", "jpeg"])],
        null=True,
        blank=True,
    )
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"ID [{self.id}] {self.name}"


class Room(models.Model):
    name = models.CharField(
        verbose_name="Name",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=255,
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
    users = models.ManyToManyField(
        verbose_name="Users",
        db_index=True,
        primary_key=False,
        editable=True,
        default="",
        max_length=100,
        to=User,
    )

    class Meta:
        app_label = "django_app"
        ordering = ("-slug", "-name")

    def __str__(self):
        return f"ID [{self.id}] {self.name}"


class Message(models.Model):
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
    room = models.ForeignKey(
        verbose_name="Room",
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=100,
        to=Room,
        on_delete=models.CASCADE,
    )
    content = models.TextField(
        verbose_name="Content",
        db_index=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
    )
    created = models.DateTimeField(
        verbose_name="Created",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default=timezone.now,
        max_length=300,
    )

    class Meta:
        app_label = "django_app"
        ordering = ("created", "-room")

    def __str__(self):
        return f"ID [{self.id}] {self.room}"
