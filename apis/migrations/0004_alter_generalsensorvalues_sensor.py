# Generated by Django 5.1.7 on 2025-03-14 21:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_remove_generalsensor_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalsensorvalues',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensor_values', to='apis.generalsensor'),
        ),
    ]
