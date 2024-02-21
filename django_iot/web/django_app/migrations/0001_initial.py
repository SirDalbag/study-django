# Generated by Django 5.0.2 on 2024-02-15 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('serial_id', models.IntegerField()),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('is_working', models.BooleanField()),
                ('fuel', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('date', models.CharField(max_length=255)),
            ],
        ),
    ]