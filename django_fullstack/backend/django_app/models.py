from django.db import models


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
