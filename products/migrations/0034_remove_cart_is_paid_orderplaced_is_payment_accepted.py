# Generated by Django 4.2.3 on 2024-02-16 11:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0033_remove_gsteighteenpercent_gst_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="is_paid",
        ),
        migrations.AddField(
            model_name="orderplaced",
            name="is_payment_accepted",
            field=models.BooleanField(default=False),
        ),
    ]
