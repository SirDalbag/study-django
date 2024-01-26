# Generated by Django 5.0.1 on 2024-01-15 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0005_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='views_count',
            field=models.PositiveIntegerField(default=0, editable=False, verbose_name='Views Count'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='is_like',
            field=models.BooleanField(blank=True, db_index=True, default=True, verbose_name='Is Like'),
        ),
    ]