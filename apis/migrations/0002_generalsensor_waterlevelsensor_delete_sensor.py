# Generated by Django 5.1.7 on 2025-03-14 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralSensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('address', models.CharField(max_length=100)),
                ('sensor_name', models.CharField(max_length=100)),
                ('notes', models.TextField()),
                ('last_service', models.DateTimeField()),
                ('installation_date', models.DateField()),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WaterLevelSensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('sensor_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('notes', models.TextField()),
                ('last_service', models.DateTimeField()),
                ('installation_date', models.DateField()),
                ('min_level', models.FloatField(default=0)),
                ('max_level', models.FloatField(default=10)),
                ('current_level', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Sensor',
        ),
    ]
