from django.urls import include, path
from .views import PoiViewSet, QuizViewSet, RewardViewSet

from rest_framework.routers import DefaultRouter

poiRouter= DefaultRouter()
poiRouter.register('',PoiViewSet,  basename='poi')

quizRouter= DefaultRouter()
quizRouter.register('',QuizViewSet,  basename='quiz')

#generalRouter.register('/value',GeneralSensorValuesViewSet,  basename='general_sensor_value')

#router= DefaultRouter()
#router.register('water_level_sensor',WaterLevelSensorViewSet,  basename='water_level_sensor')


urlpatterns = [
    path('poi/',  include( poiRouter.urls)),
    path('quiz/',  include( quizRouter.urls)),
    path('reward/', RewardViewSet.as_view()),
]
