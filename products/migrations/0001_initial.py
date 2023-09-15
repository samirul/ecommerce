# Generated by Django 4.2.3 on 2023-09-14 08:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Categories",
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
                ("category_name", models.CharField(max_length=150)),
                ("category_description", models.CharField(max_length=150)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Coupon",
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
                ("coupon_code", models.CharField(max_length=10)),
                ("is_expired", models.BooleanField(default=False)),
                ("discount_price", models.IntegerField(default=0)),
                ("minimum_amount", models.IntegerField(default=0)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Subcategories",
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
                ("subcategory_name", models.CharField(max_length=150)),
                (
                    "categories",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.categories",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Products",
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
                ("product_title", models.CharField(max_length=150)),
                ("product_slug", models.SlugField(blank=True, null=True, unique=True)),
                ("product_selling_price", models.FloatField()),
                ("product_discounted_price", models.FloatField()),
                ("product_description", models.CharField(max_length=255)),
                ("product_image", models.ImageField(upload_to="product_imgs")),
                ("brand", models.CharField(max_length=150)),
                (
                    "categories",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.categories",
                    ),
                ),
                (
                    "subcategories",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.subcategories",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="OrderPlaced",
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
                ("quantity", models.PositiveIntegerField(default=1)),
                ("ordered_date", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Accepted", "Accepted"),
                            ("Packed", "Packed"),
                            ("On The Way", "On The Way"),
                            ("Delivered", "Delivered"),
                            ("Cancel", "Cancel"),
                        ],
                        default="Pending",
                        max_length=50,
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.products",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Cart",
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
                ("quantity", models.PositiveIntegerField(default=1)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.products",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
