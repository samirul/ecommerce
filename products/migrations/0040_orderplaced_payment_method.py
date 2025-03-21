# Generated by Django 4.2.3 on 2024-02-17 20:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0039_cart_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderplaced",
            name="payment_method",
            field=models.CharField(
                choices=[
                    ("Cash on Delivery", "Cash on Delivery"),
                    ("Online Payment", "Online Payment"),
                ],
                default="",
                max_length=100,
            ),
        ),
    ]
