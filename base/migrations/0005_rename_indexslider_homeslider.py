# Generated by Django 4.2.3 on 2023-09-16 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0004_rename_slider_indexslider"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="IndexSlider",
            new_name="HomeSlider",
        ),
    ]
