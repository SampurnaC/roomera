# Generated by Django 4.2.17 on 2025-01-11 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landlord_property', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='property',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='landlord_property.property'),
            preserve_default=False,
        ),
    ]