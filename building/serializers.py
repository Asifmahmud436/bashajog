from rest_framework import serializers
from .models import Building,Unit

class BuildingSerializer(serializers.Serializer):
    class Meta:
        model = Building
        fields = '__all__'

class UnitSerializer(serializers.Serializer):
    class Meta:
        model = Unit
        fields = '__all__'