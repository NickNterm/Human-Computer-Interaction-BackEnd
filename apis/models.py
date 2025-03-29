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

class POI(models.Model):
    lat= models.FloatField()
    lon= models.FloatField()
    type = models.CharField(max_length=100)
    name= models.CharField(max_length=100)
    imageUrl = models.CharField(max_length=100)
    shortDescription = models.CharField(max_length=1000)
    longDescription = models.TextField()

    def __str__(self):
        return self.name

class Stores(models.Model):
    lat= models.FloatField()
    lon= models.FloatField()
    name = models.CharField(max_length=100)
    imageUrl = models.CharField(max_length=1000)
    description = models.TextField()

    def __str__(self):
        return self.name


class Quiz(models.Model):
    poi = models.ForeignKey(POI, on_delete=models.CASCADE)
    questions= models.ManyToManyField('Question')

class Question(models.Model):
    question = models.CharField(max_length=1000)
    choice1= models.CharField(max_length=100)
    choice2= models.CharField(max_length=100)
    choice3= models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.question

class Reward(models.Model):
    name = models.CharField(max_length=100)
    store = models.ForeignKey(Stores, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

