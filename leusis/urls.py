
from django.urls import include, path
from .views import ProjectViewSet, TodoViewSet

from rest_framework.routers import DefaultRouter


todoRouter= DefaultRouter()
todoRouter.register('', TodoViewSet,  basename='todo')

projectRouter= DefaultRouter()
projectRouter.register('', ProjectViewSet,  basename='projecttt')

urlpatterns = [
    path('todo/',  include( todoRouter.urls)),
    path('project/',  include( projectRouter.urls)),
]
