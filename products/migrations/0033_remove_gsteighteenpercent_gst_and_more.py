# Generated by Django 4.2.3 on 2024-02-08 07:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "products",
            "0032_alter_gst_options_alter_gsteighteenpercent_options_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="gsteighteenpercent",
            name="gst",
        ),
        migrations.RemoveField(
            model_name="gstfivepercent",
            name="gst",
        ),
        migrations.RemoveField(
            model_name="gsttwelvepercent",
            name="gst",
        ),
        migrations.RemoveField(
            model_name="gstzeropercent",
            name="gst",
        ),
        migrations.DeleteModel(
            name="GST",
        ),
        migrations.DeleteModel(
            name="GSTEighteenPercent",
        ),
        migrations.DeleteModel(
            name="GSTFivePercent",
        ),
        migrations.DeleteModel(
            name="GSTTwelvePercent",
        ),
        migrations.DeleteModel(
            name="GSTZeroPercent",
        ),
    ]
