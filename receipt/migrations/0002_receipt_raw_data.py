# Generated by Django 4.1.7 on 2023-05-05 08:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("receipt", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="receipt",
            name="raw_data",
            field=models.JSONField(null=True),
        ),
    ]
