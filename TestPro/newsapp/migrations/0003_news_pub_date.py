# Generated by Django 4.2.13 on 2024-06-04 12:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0002_sportsnews'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='pub_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
