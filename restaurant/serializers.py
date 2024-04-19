from rest_framework import serializers
from .models import Menu
from .models import Booking

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'  # You can specify specific fields if needed


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'  # You can specify specific fields if needed