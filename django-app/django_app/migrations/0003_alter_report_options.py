# Generated by Django 5.0 on 2024-01-06 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0002_alter_report_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'ordering': ('status', 'id', '-date'), 'verbose_name': 'Report', 'verbose_name_plural': 'Reports'},
        ),
    ]
