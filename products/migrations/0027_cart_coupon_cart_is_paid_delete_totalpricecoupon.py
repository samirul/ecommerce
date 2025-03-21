# Generated by Django 4.2.3 on 2023-11-29 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0026_remove_totalpricecoupon_cart_totalpricecoupon_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="coupon",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="products.coupon",
            ),
        ),
        migrations.AddField(
            model_name="cart",
            name="is_paid",
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name="TotalPriceCoupon",
        ),
    ]
