# Generated by Django 5.0.1 on 2024-01-20 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='Product has no description', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='product/qr-codes/'),
        ),
    ]
