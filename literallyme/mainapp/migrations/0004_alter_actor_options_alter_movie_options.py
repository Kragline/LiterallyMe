# Generated by Django 4.2.4 on 2023-08-09 16:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0003_alter_actor_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="actor",
            options={
                "verbose_name": "Actors (they are literally me)",
                "verbose_name_plural": "Actors (they are literally me)",
            },
        ),
        migrations.AlterModelOptions(
            name="movie",
            options={
                "verbose_name": "Movies (literally me)",
                "verbose_name_plural": "Movies (literally me)",
            },
        ),
    ]
