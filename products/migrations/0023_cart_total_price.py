# Generated by Django 4.2.3 on 2023-11-26 18:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0022_cart_coupon_cart_is_paid"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="total_price",
            field=models.IntegerField(default=0),
        ),
    ]
