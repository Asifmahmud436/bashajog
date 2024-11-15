from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.Serializer):
    class Meta:
        model = Booking
        fields = '__all__'