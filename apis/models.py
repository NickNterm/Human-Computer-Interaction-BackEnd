from django.db import models

class GeneralSensor(models.Model):
    lat= models.FloatField()
    lon= models.FloatField()
    address = models.CharField(max_length=100)
    sensor_name = models.CharField(max_length=100)
    notes= models.TextField()
    last_service = models.DateTimeField()
    installation_date= models.DateField()
    sensor_type = models.CharField(max_length=100)
    min_value = models.FloatField(default=1)
    max_value = models.FloatField(default=15)
    

    def __str__(self):
        return self.sensor_name

class GeneralSensorValues(models.Model):
    sensor = models.ForeignKey(GeneralSensor, on_delete=models.CASCADE, related_name='sensor_values')
    data = models.TextField()
    date = models.DateTimeField() 

    def __str__(self):
        return self.sensor.sensor_name


# Create your models here.
class WaterLevelSensor(models.Model):
    lat= models.FloatField()
    lon= models.FloatField()
    sensor_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    notes= models.TextField()
    last_service = models.DateTimeField()
    installation_date= models.DateField()
    min_level = models.FloatField(default=0)
    max_level = models.FloatField(default=10)

    def __str__(self):
        return self.sensor_name

class WaterLevelSensorValues(models.Model):
    sensor = models.ForeignKey(WaterLevelSensor, on_delete=models.CASCADE)
    level = models.FloatField()
    date = models.DateTimeField()

    def __str__(self):
        return self.sensor.sensor_name


class NotifiedUser(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=100)

    def __str__(self):
        return self.name

