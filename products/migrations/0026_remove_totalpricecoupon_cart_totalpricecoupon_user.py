# Generated by Django 4.2.3 on 2023-11-29 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("products", "0025_totalpricecoupon_cart"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="totalpricecoupon",
            name="cart",
        ),
        migrations.AddField(
            model_name="totalpricecoupon",
            name="user",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
