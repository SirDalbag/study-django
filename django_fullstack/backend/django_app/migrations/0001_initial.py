# Generated by Django 5.0.2 on 2024-02-26 15:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Категория')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('slug', models.SlugField(unique=True, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Книга')),
                ('author', models.CharField(max_length=255, verbose_name='Автор')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('publish_date', models.DateField(verbose_name='Дата публикации')),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='book_covers/', verbose_name='Обложка')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='django_app.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]
