# Generated by Django 5.0 on 2024-01-06 06:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(db_index=True, default=None, max_length=12, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.MinLengthValidator(12), django.core.validators.MaxLengthValidator(12)], verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=200, verbose_name='Name')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Price')),
                ('image', models.FileField(upload_to='static/src/products')),
                ('status', models.BooleanField(default=True, verbose_name='Availability')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ('status', '-price'),
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(db_index=True, default=None, max_length=12, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.MinLengthValidator(12), django.core.validators.MaxLengthValidator(12)], verbose_name='ID')),
                ('email', models.CharField(blank=True, default='', max_length=200, verbose_name='Email')),
                ('report', models.CharField(blank=True, default='', max_length=200, verbose_name='Report')),
                ('type', models.CharField(blank=True, default='', max_length=50, verbose_name='Type')),
                ('date', models.CharField(blank=True, default='', max_length=50, verbose_name='Date')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Report',
                'verbose_name_plural': 'Reports',
                'ordering': ('status', 'id'),
            },
        ),
    ]
