# Generated by Django 5.0.2 on 2024-02-26 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0002_remove_category_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='category',
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(related_name='books', to='django_app.category', verbose_name='Категория'),
        ),
    ]