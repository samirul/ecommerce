# Generated by Django 4.2.3 on 2023-11-13 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0021_alter_servicebigimage_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="servicebigimage",
            name="services",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="service_big_image",
                to="base.services",
            ),
        ),
        migrations.AlterField(
            model_name="serviceimages",
            name="services",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="service_images",
                to="base.services",
            ),
        ),
        migrations.AlterField(
            model_name="servicerowtexts",
            name="services",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="service_row_texts",
                to="base.services",
            ),
        ),
    ]
