# Generated by Django 4.2.3 on 2023-09-18 07:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0006_alter_products_subcategories"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tags",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_by", models.DateTimeField(auto_now_add=True)),
                ("updated_by", models.DateTimeField(auto_now=True)),
                ("innerTag", models.CharField(max_length=150)),
                ("homeTag", models.CharField(max_length=150)),
                (
                    "products",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.products",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
