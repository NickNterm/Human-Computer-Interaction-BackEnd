from django.contrib import admin

# Register your models here.

from .models import Project, Todo
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('id',)
    list_per_page = 10
    list_editable = ('name',)
    
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'priority', 'project')
    search_fields = ('name', 'description')
    list_filter = ('priority',)
    ordering = ('id',)
    list_per_page = 10
    list_editable = ('name', 'description', 'priority')
