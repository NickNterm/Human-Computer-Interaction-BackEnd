from rest_framework import serializers
from .models import  POI, Quiz, Question, Reward, Stores

class PoiSerializer(serializers.ModelSerializer):
    class Meta:
        model = POI
        fields = ['id', 'lat', 'lon', 'type', 'name', 'imageUrl', 'shortDescription', 'longDescription']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question', 'choice1', 'choice2', 'choice3', 'answer']

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Quiz
        fields = ['questions']


class StoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stores
        fields = ['id',  'imageUrl', 'lat', 'lon' ,'name', 'description']


class RewardSerializer(serializers.ModelSerializer):
    store = StoresSerializer(many=False)
    class Meta:
        model = Reward
        fields = ['id', 'name', 'is_active', 'store']

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
