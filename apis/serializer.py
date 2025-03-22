from rest_framework import serializers
from .models import GeneralSensor, WaterLevelSensor, GeneralSensorValues, WaterLevelSensorValues


class GetGeneralSensorValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralSensorValues
        #exclude = ['sensor']
        fields = ['id', 'data', 'date']

class PostGeneralSensorValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralSensorValues
        fields = ['id', 'data', 'date', 'sensor']

class GeneralSensorSerializer(serializers.ModelSerializer):
    sensor_values = GetGeneralSensorValuesSerializer(many=True, read_only=True,data=GeneralSensorValues.objects.all())

    class Meta:
        model = GeneralSensor
        fields = ['id', 'lat', 'lon', 'address', 'sensor_name', 'notes','sensor_type','min_value','max_value', 'last_service', 'installation_date', 'sensor_values']
        read_only_fields = ['id', 'sensor_values']
        

class WaterLevelSensorValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterLevelSensorValues
        fields = '__all__'

class WaterLevelSensorSerializer(serializers.ModelSerializer):
    sensor_values = WaterLevelSensorValuesSerializer(many=True, read_only=True)
    class Meta:
        model = WaterLevelSensor
        fields = '__all__'
