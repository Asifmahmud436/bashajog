from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    unit_name = serializers.CharField(source='unit.name',read_only=True)
    building_name = serializers.CharField(source='unit.building.name',read_only=True)
    tenant_name = serializers.CharField(source='tenant.user.username',read_only=True)
    
    class Meta:
        model = Booking
        fields = '__all__'