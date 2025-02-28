# Generated by Django 4.2 on 2025-02-28 00:30

import django.contrib.postgres.indexes
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="chargingstation",
            index=models.Index(fields=["name"], name="api_chargin_name_437959_idx"),
        ),
        migrations.AddIndex(
            model_name="chargingstation",
            index=models.Index(fields=["city"], name="api_chargin_city_c56ebf_idx"),
        ),
        migrations.AddIndex(
            model_name="chargingstation",
            index=django.contrib.postgres.indexes.GistIndex(
                fields=["location"], name="api_chargin_locatio_f6a639_gist"
            ),
        ),
    ]
