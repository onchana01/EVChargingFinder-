from rest_framework import serializers
from .models import ChargingStation, Reservation, StationUsage

class ChargingStationSerializer(serializers.ModelSerializer):
    latitude = serializers.FloatField(source='location.y')
    longitude = serializers.FloatField(source='location.x')

    class Meta:
        model = ChargingStation
        fields = ('station_id', 'name', 'city', 'latitude', 'longitude', 'power_kw',
            'connector_types', 'price_eur_per_kwh', 'availability', 'renewable')

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('id', 'user', 'station', 'start_time', 'end_time', 'created_at')

class StationUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StationUsage
        fields = ('id', 'station', 'energy_dispensed_kwh', 'timestamp')