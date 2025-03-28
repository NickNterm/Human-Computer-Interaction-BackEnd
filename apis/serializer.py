from rest_framework import serializers
from .models import GeneralSensor, GeneralSensorValues, POI, Quiz, Question, Reward, Stores

class PoiSerializer(serializers.ModelSerializer):
    class Meta:
        model = POI
        fields = ['id', 'lat', 'lon', 'type', 'name', 'imageUrl', 'shortDescription', 'longDescription']

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'questions']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question', 'choice1', 'choice2', 'choice3', 'answer']

class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = ['id', 'name']

class StoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stores
        fields = ['id', 'lat', 'lon', 'name', 'imageUrl', 'description']

# class GetGeneralSensorValuesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GeneralSensorValues
#         #exclude = ['sensor']
#         fields = ['id', 'data', 'date']
# 
# class PostGeneralSensorValuesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GeneralSensorValues
#         fields = ['id', 'data', 'date', 'sensor']
# 
# class GeneralSensorSerializer(serializers.ModelSerializer):
#     sensor_values = GetGeneralSensorValuesSerializer(many=True, read_only=True,data=GeneralSensorValues.objects.all())
# 
#     class Meta:
#         model = GeneralSensor
#         fields = ['id', 'lat', 'lon', 'address', 'sensor_name', 'notes','sensor_type','min_value','max_value', 'last_service', 'installation_date', 'sensor_values']
#         read_only_fields = ['id', 'sensor_values']
#         
