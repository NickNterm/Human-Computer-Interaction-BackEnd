from django.urls import include, path
from .views import GeneralSensorValuesViewSet, GeneralSensorViewSet, WaterLevelSensorViewSet

from rest_framework.routers import DefaultRouter

generalRouter = DefaultRouter()
generalRouter.register('/sensor', GeneralSensorViewSet,  basename='general_sensor')
generalRouter.register('/value',GeneralSensorValuesViewSet,  basename='general_sensor_value')

router= DefaultRouter()
router.register('water_level_sensor',WaterLevelSensorViewSet,  basename='water_level_sensor')


urlpatterns = [
    path('general',  include( generalRouter.urls)),
    path('water',  include(router.urls)),
]
