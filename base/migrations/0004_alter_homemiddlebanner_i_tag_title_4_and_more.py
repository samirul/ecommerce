# Generated by Django 4.2.3 on 2023-10-13 17:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0003_alter_homemiddlebanner_i_tag_title_4_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homemiddlebanner",
            name="i_tag_title_4",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name="homemiddlebanner",
            name="title_1",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name="homemiddlebanner",
            name="title_2",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name="homemiddlebanner",
            name="title_3",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
