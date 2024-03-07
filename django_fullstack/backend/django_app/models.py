from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(verbose_name="Категория", max_length=255, unique=True)
    slug = models.SlugField(verbose_name="Ссылка", unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(verbose_name="Тег", max_length=255, unique=True)
    slug = models.SlugField(verbose_name="Ссылка", unique=True)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(verbose_name="Книга", max_length=255)
    author = models.CharField(verbose_name="Автор", max_length=255)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    short_description = models.CharField(
        verbose_name="Короткое описание", max_length=255, blank=True, null=True
    )
    categories = models.ManyToManyField(
        Category,
        verbose_name="Категории",
        related_name="books",
    )
    tags = models.ManyToManyField(
        Tag, verbose_name="Теги", related_name="books", blank=True
    )
    publish_date = models.DateField(verbose_name="Дата публикации")
    cover_image = models.ImageField(
        verbose_name="Обложка", upload_to="book_covers/", null=True, blank=True
    )

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return f"{self.title} - {self.author}"


class Token(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    token = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.token

    @property
    def is_expired(self):
        return timezone.now() - self.created_at > timezone.timedelta(hours=1)


class Log(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        db_index=True,
    )
    ip = models.CharField(max_length=40, null=False, blank=True, db_index=True)
    date = models.DateTimeField(
        default=timezone.now, null=False, blank=True, db_index=True
    )

    def __str__(self):
        return f"{self.ip} - {self.date}"
