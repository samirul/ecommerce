# Generated by Django 4.2.3 on 2023-10-18 09:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0016_alter_cart_quantity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="quantity",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
