from django.contrib import admin
from apis import models

# Register your models here.
class POIAdmin(admin.ModelAdmin):
    list_display = ('name', 'lat', 'lon', 'type')
    search_fields = ('name', 'type')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice1', 'choice2', 'choice3', 'answer')
    search_fields = ('question', 'answer')

class RewardAdmin(admin.ModelAdmin):
    list_display = ('name','is_active')
    search_fields = ('name','is_active')

class StoresAdmin(admin.ModelAdmin):
    list_display = ('name', 'lat', 'lon', 'description')
    search_fields = ('name', 'description')

class QuizAdmin(admin.ModelAdmin):
    list_display = ('poi',)
    search_fields = ('poi',)

admin.site.register(models.POI, POIAdmin)
admin.site.register(models.Quiz, QuizAdmin)
admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Reward, RewardAdmin)
admin.site.register(models.Stores, StoresAdmin)
# class GeneralSensorAdmin(admin.ModelAdmin):
#     list_display = ('sensor_name', 'last_service', 'installation_date')
#     search_fields = ('sensor_name', 'address')
# 
# class GeneralSensorValuesAdmin(admin.ModelAdmin):
#     list_display = ('sensor', 'data', 'date')
#     search_fields = ('sensor', 'data')
# 
# class NotifiedUserAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'group')
#     search_fields = ('name', 'group', 'email')
# 
# admin.site.register(models.GeneralSensor, GeneralSensorAdmin)
# admin.site.register(models.GeneralSensorValues, GeneralSensorValuesAdmin)
# admin.site.register(models.NotifiedUser, NotifiedUserAdmin)
