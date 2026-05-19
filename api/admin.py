# api/admin.py
from django.contrib import admin
from .models import Vehiculo  

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('id', 'marca', 'localidad', 'aspirante')
    search_fields = ('marca', 'aspirante')