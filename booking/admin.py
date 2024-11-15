from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['unit_name','rent','is_booked','tenant_name']


    def unit_name(self,obj):
        return obj.unit.name

    def tenant_name(self,obj):
        return obj.tenant.user.username
