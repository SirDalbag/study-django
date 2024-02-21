# Generated by Django 5.0.1 on 2024-01-29 04:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0005_room_users'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('created', '-room')},
        ),
        migrations.AlterField(
            model_name='room',
            name='users',
            field=models.ManyToManyField(db_index=True, default='', max_length=100, to=settings.AUTH_USER_MODEL, verbose_name='Users'),
        ),
    ]