# Generated by Django 4.2.3 on 2024-02-02 16:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0030_gsteighteenpercent_gstzero_percent_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="GST",
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
                (
                    "name",
                    models.CharField(
                        default="Add GST Information", editable=False, max_length=50
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.RemoveField(
            model_name="gsteighteenpercent",
            name="gstzero_percent",
        ),
        migrations.RemoveField(
            model_name="gstfivepercent",
            name="gstzero_percent",
        ),
        migrations.RemoveField(
            model_name="gsttwelvepercent",
            name="gstzero_percent",
        ),
        migrations.AddField(
            model_name="gsteighteenpercent",
            name="gst",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="products.gst",
            ),
        ),
        migrations.AddField(
            model_name="gstfivepercent",
            name="gst",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="products.gst",
            ),
        ),
        migrations.AddField(
            model_name="gsttwelvepercent",
            name="gst",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="products.gst",
            ),
        ),
        migrations.AddField(
            model_name="gstzeropercent",
            name="gst",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="products.gst",
            ),
        ),
    ]
