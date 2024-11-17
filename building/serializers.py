from rest_framework import serializers
from .models import Building,Unit

class BuildingSerializer(serializers.ModelSerializer):
    owner_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Building
        fields = '__all__'
    
    def get_owner_name(self,obj):
        return [{'first_name':owner.user.first_name,'last_name':owner.user.last_name} for owner in obj.owner.all()]
    
class UnitSerializer(serializers.ModelSerializer):
    building_name = serializers.CharField(source='building.name',read_only=True)
    tenant_name = serializers.CharField(source='tenant.user.username',read_only=True)
    class Meta:
        model = Unit
        fields = '__all__'