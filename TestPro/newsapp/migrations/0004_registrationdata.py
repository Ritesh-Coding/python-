# Generated by Django 4.2.13 on 2024-06-04 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0003_news_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
    ]
