# Generated by Django 5.0 on 2023-12-25 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='static/src/'),
        ),
    ]