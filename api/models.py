from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.indexes import GistIndex

class ChargingStation(models.Model):
    station_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    location = models.PointField()  # Latitude/longitude stored as a geospatial point
    power_kw = models.IntegerField()
    connector_types = models.JSONField()  # e.g., ["CCS", "Type 2"]
    price_eur_per_kwh = models.FloatField()
    availability = models.CharField(max_length=20, choices=[
        ('Available', 'Available'),
        ('Occupied', 'Occupied'),
        ('Maintenance', 'Maintenance'),
    ])
    renewable = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['city']),
            GistIndex(fields=['location']),  # For geospatial queries
        ]

    

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    station = models.ForeignKey(ChargingStation, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

class StationUsage(models.Model):
    station = models.ForeignKey(ChargingStation, on_delete=models.CASCADE)
    energy_dispensed_kwh = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)