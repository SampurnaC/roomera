# Generated by Django 4.2.17 on 2025-02-05 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landlord_property', '0003_rename_city_property_postcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
