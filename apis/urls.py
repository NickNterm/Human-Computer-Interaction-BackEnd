from django.urls import include, path
from .views import PoiViewSet

from rest_framework.routers import DefaultRouter

poiRouter= DefaultRouter()
poiRouter.register('/poi',PoiViewSet,  basename='poi')
#generalRouter.register('/value',GeneralSensorValuesViewSet,  basename='general_sensor_value')

#router= DefaultRouter()
#router.register('water_level_sensor',WaterLevelSensorViewSet,  basename='water_level_sensor')


urlpatterns = [
    path('poi',  include( poiRouter.urls)),
    #path('water',  include(router.urls)),
]
