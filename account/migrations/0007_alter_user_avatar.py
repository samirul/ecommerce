# Generated by Django 4.2.3 on 2023-10-05 10:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0006_alter_user_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                blank=True, default="profileimage.png", upload_to="profiles"
            ),
        ),
    ]
