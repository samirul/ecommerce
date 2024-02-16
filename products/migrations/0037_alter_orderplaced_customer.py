# Generated by Django 4.2.3 on 2024-02-16 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0016_remove_user_is_verified_alter_user_is_active"),
        ("products", "0036_orderplaced_customer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderplaced",
            name="customer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="account.customer"
            ),
        ),
    ]
