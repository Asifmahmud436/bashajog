from django.contrib import admin
from .models import Unit,Building

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['name','room','building_name']

    def building_name(self,obj):
        return obj.building.name

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ['name','address','owner_name']

    def owner_name(self,obj):
        return obj.owner.user.username

