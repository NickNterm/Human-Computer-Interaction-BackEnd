from django.contrib import admin
from apis import models

# Register your models here.
class GeneralSensorAdmin(admin.ModelAdmin):
    list_display = ('sensor_name', 'last_service', 'installation_date')
    search_fields = ('sensor_name', 'address')

class GeneralSensorValuesAdmin(admin.ModelAdmin):
    list_display = ('sensor', 'data', 'date')
    search_fields = ('sensor', 'data')

class NotifiedUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'group')
    search_fields = ('name', 'group', 'email')

admin.site.register(models.GeneralSensor, GeneralSensorAdmin)
admin.site.register(models.GeneralSensorValues, GeneralSensorValuesAdmin)
admin.site.register(models.NotifiedUser, NotifiedUserAdmin)