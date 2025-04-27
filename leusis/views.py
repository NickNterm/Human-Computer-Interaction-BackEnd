from rest_framework import (
    viewsets,
    mixins,
)

from leusis.models import Project, Todo
from leusis.serializer import ProjectSerializer, TodoSerializer


class TodoViewSet(mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.CreateModelMixin,
                 viewsets.GenericViewSet):

    queryset =Todo.objects.all()
    serializer_class = TodoSerializer


class ProjectViewSet(mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.CreateModelMixin,
                 viewsets.GenericViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
