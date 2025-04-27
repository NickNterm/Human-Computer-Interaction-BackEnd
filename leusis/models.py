from django.db import models
from django_enum import EnumField

class Project(models.Model):
    name = models.CharField(max_length = 20)

class Todo(models.Model):
    name = models.CharField(max_length=20)
    description= models.TextField()

    class PriorityEnum(models.IntegerChoices):
        LOW = 1, "Minimum"
        MED = 2, "Medium"
        MAX = 3, "Maximum"

    priority= EnumField( PriorityEnum, default= PriorityEnum.LOW)
    project = models.ForeignKey( Project, on_delete=models.CASCADE, blank=True,null=True)

    

