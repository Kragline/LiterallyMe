# Generated by Django 4.2.4 on 2023-08-21 18:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0007_rename_comments_comment"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="create_date",
            new_name="create_time",
        ),
    ]