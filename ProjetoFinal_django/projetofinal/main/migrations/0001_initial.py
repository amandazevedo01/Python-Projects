# Generated by Django 4.1 on 2022-12-28 09:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjetoDjango',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=50)),
                ('data', models.DateTimeField(default=datetime.datetime(2022, 12, 28, 20, 7, 46, 723414), verbose_name='Publicado em')),
            ],
        ),
    ]