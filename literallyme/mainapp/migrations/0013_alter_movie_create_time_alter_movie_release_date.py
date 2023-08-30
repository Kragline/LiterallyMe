# Generated by Django 4.2.4 on 2023-08-30 17:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0012_movie_trailer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="create_time",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="movie",
            name="release_date",
            field=models.DateField(default=datetime.date.today),
        ),
    ]
