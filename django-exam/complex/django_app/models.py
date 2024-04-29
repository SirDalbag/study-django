from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(
        to=User, null=False, blank=False, verbose_name="User", on_delete=models.CASCADE
    )
    title = models.CharField(
        verbose_name="Title",
        max_length=150,
        blank=False,
        null=False,
    )
    text = models.TextField(
        verbose_name="Text",
        blank=False,
        null=False,
    )
    created_at = models.DateTimeField(
        verbose_name="Created At", auto_now_add=True, null=False, blank=True
    )

    class Meta:
        app_label = "django_app"
        ordering = ("-created_at",)
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"


class Comment(models.Model):
    user = models.ForeignKey(
        to=User, null=False, blank=False, verbose_name="User", on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        to=Post, null=False, blank=False, verbose_name="Post", on_delete=models.CASCADE
    )
    text = models.TextField(
        verbose_name="Text",
        blank=False,
        null=False,
    )
    created_at = models.DateTimeField(
        verbose_name="Created At", auto_now_add=True, null=False, blank=True
    )

    class Meta:
        app_label = "django_app"
        ordering = ("-created_at",)
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"{self.user.username} - {self.post}"
