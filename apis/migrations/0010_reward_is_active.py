# Generated by Django 5.1.7 on 2025-03-28 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0009_stores_lat_stores_lon'),
    ]

    operations = [
        migrations.AddField(
            model_name='reward',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
