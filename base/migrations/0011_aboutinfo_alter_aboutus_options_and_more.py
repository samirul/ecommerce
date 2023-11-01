# Generated by Django 4.2.3 on 2023-11-01 17:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0010_aboutlist_alter_contactinfo_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="AboutInfo",
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
                ("information", models.TextField(max_length=2000)),
                ("about_img", models.ImageField(upload_to="about")),
            ],
            options={
                "verbose_name_plural": "About Info",
            },
        ),
        migrations.AlterModelOptions(
            name="aboutus",
            options={"verbose_name_plural": "About Us"},
        ),
        migrations.RemoveField(
            model_name="aboutus",
            name="about_img",
        ),
        migrations.RemoveField(
            model_name="aboutus",
            name="information",
        ),
        migrations.RemoveField(
            model_name="aboutus",
            name="list_info",
        ),
        migrations.DeleteModel(
            name="AboutList",
        ),
        migrations.AddField(
            model_name="aboutus",
            name="about_info",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="base.aboutinfo",
            ),
        ),
    ]
