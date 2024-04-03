from django.db import models
import datetime


# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name="Должность")

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"

    def __str__(self):
        return f"{self.title}"


class Person(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, db_index=True, verbose_name="Фамилия")
    patranomic = models.CharField(max_length=100, verbose_name="Отчество")
    tabel_num = models.CharField(
        unique=True, max_length=24, db_index=True, verbose_name="Табельный номер"
    )
    position = models.ForeignKey(
        to=Position, on_delete=models.SET_NULL, null=True, verbose_name="Должность"
    )

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return f"{self.tabel_num} - {self.last_name} - {self.position.title}"


class ClothCategory(models.Model):
    title = models.CharField(max_length=100, db_index=True)

    class Meta:
        verbose_name = "Категория одежды"
        verbose_name_plural = "Категории одежды"

    def __str__(self):
        return f"{self.title}"


class Cloth(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(to=ClothCategory, on_delete=models.SET_NULL, null=True)
    deadline = models.IntegerField()

    class Meta:
        verbose_name = "Одежда"
        verbose_name_plural = "Одежды"

    def __str__(self):
        return f"{self.title} - {self.category.title}"


class ClothSet(models.Model):
    person = models.ForeignKey(to=Person, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    cloth_type = models.ForeignKey(to=Cloth, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Выдача"
        verbose_name_plural = "Выдачи"

    def __str__(self):
        return f"{self.created_at} - {self.person.tabel_num} ({self.person.last_name}) - {self.is_active}, {self.cloth_type.title}"

    @property
    def get_end_date(self):
        if self.cloth_type and self.cloth_type.deadline:
            return self.created_at + datetime.timedelta(days=self.cloth_type.deadline)
        else:
            return None
