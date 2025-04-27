from rest_framework import serializers

from leusis.models import Project, Todo



class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "name", "description", "priority"]

class ProjectSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many = True)
    class Meta:
        model = Project
        fields = ["id", "name", "todos"]
