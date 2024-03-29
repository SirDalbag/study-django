# Generated by Django 5.0.2 on 2024-02-26 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0006_remove_book_tags_delete_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Тег')),
                ('slug', models.SlugField(unique=True, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='books', to='django_app.tag', verbose_name='Теги'),
        ),
    ]
