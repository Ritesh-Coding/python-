# Generated by Django 4.2.13 on 2024-06-04 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SportsNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
    ]
