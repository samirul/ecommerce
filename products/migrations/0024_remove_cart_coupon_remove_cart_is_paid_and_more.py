# Generated by Django 4.2.3 on 2023-11-26 18:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0023_cart_total_price"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="coupon",
        ),
        migrations.RemoveField(
            model_name="cart",
            name="is_paid",
        ),
        migrations.RemoveField(
            model_name="cart",
            name="total_price",
        ),
        migrations.CreateModel(
            name="TotalPriceCoupon",
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
                ("total_price", models.IntegerField(default=0)),
                ("is_paid", models.BooleanField(default=False)),
                (
                    "coupon",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="products.coupon",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
