# Generated by Django 5.1.7 on 2025-03-28 18:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0007_generalsensor_max_value_generalsensor_min_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='POI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('type', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('imageUrl', models.CharField(max_length=100)),
                ('shortDescription', models.CharField(max_length=1000)),
                ('longDescription', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('choice1', models.CharField(max_length=100)),
                ('choice2', models.CharField(max_length=100)),
                ('choice3', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.poi')),
                ('questions', models.ManyToManyField(to='apis.question')),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Stores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('imageUrl', models.CharField(max_length=1000)),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='NotifiedUser',
        ),
        migrations.RemoveField(
            model_name='waterlevelsensorvalues',
            name='sensor',
        ),
        migrations.DeleteModel(
            name='WaterLevelSensor',
        ),
        migrations.DeleteModel(
            name='WaterLevelSensorValues',
        ),
    ]
