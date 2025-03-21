# Generated by Django 4.2.3 on 2024-02-02 17:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0031_gst_remove_gsteighteenpercent_gstzero_percent_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="gst",
            options={"verbose_name_plural": "GST"},
        ),
        migrations.AlterModelOptions(
            name="gsteighteenpercent",
            options={"verbose_name_plural": "GST Eighteen Percent"},
        ),
        migrations.AlterModelOptions(
            name="gstfivepercent",
            options={"verbose_name_plural": "GST Five Percent"},
        ),
        migrations.AlterModelOptions(
            name="gsttwelvepercent",
            options={"verbose_name_plural": "GST Twelve Percent"},
        ),
        migrations.AlterModelOptions(
            name="gstzeropercent",
            options={"verbose_name_plural": "GST Zero Percent"},
        ),
    ]
