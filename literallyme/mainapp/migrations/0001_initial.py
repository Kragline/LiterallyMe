# Generated by Django 4.2.4 on 2023-08-05 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Actor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("bio", models.TextField(blank=True)),
                ("photo", models.ImageField(upload_to="photos/%d/%m/%Y")),
                ("create_time", models.DateTimeField(auto_now_add=True)),
                ("slug", models.SlugField(max_length=255, unique=True)),
            ],
            options={
                "verbose_name": "Actors (they are literally me)",
                "verbose_name_plural": "Actors (they are literally me)",
                "ordering": ["create_time", "name"],
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("slug", models.SlugField(max_length=255, unique=True)),
            ],
            options={
                "verbose_name": "Categories (literally me)",
                "verbose_name_plural": "Categories (literally me)",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("plot", models.TextField(blank=True)),
                ("release_date", models.CharField(max_length=100)),
                ("poster", models.ImageField(upload_to="posters/%d/%m/%Y")),
                ("create_time", models.DateTimeField(auto_now_add=True, null=True)),
                ("slug", models.SlugField(max_length=255, unique=True)),
                (
                    "actors",
                    models.ManyToManyField(related_name="movies", to="mainapp.actor"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="mainapp.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Movies (literally me)",
                "verbose_name_plural": "Movies (literally me)",
                "ordering": ["create_time", "title"],
            },
        ),
    ]
