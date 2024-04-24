from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(
        to=User,
        blank=True,
        null=False,
        verbose_name="Пользователь",
        related_name="profile",
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name="Имя",
        blank=True,
        null=False,
        max_length=100,
    )
    avatar = models.ImageField(
        verbose_name="Аватар",
        validators=[FileExtensionValidator(["jpg", "png", "jpeg", "svg"])],
        unique=False,
        editable=True,
        blank=False,
        null=False,
        default="profile/avatars/default.svg",
        upload_to="profile/avatars",
    )
    bio = models.TextField(
        verbose_name="Биография",
        blank=False,
        null=True,
        max_length=150,
    )

    class Meta:
        app_label = "django_app"
        ordering = ("-user",)
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return f"{self.user} - {self.name}"


@receiver(post_save, sender=User)
def profile_create(sender, instance, created, **kwargs):
    try:
        Profile.objects.get(user=instance)
    except Exception:
        Profile.objects.create(user=instance, name=instance.username)


class Post(models.Model):
    user = models.ForeignKey(
        to=User,
        null=False,
        blank=False,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
    )
    text = models.TextField(
        verbose_name="Текст",
        blank=True,
        null=True,
        max_length=255,
    )
    creation_date = models.DateTimeField(
        verbose_name="Дата создания", auto_now_add=True, null=False, blank=True
    )

    class Meta:
        app_label = "django_app"
        ordering = ("-creation_date",)
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return f"{self.user.username} - {self.creation_date}"


class Comment(models.Model):
    user = models.ForeignKey(
        to=User,
        null=False,
        blank=False,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        to=Post, null=False, blank=True, verbose_name="Пост", on_delete=models.CASCADE
    )
    text = models.TextField(
        verbose_name="Текст",
        blank=True,
        null=True,
        max_length=255,
    )
    creation_date = models.DateTimeField(
        verbose_name="Дата создания", auto_now_add=True, null=False, blank=True
    )

    class Meta:
        app_label = "django_app"
        ordering = ("-creation_date",)
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f"{self.user.username} - {self.post}"
