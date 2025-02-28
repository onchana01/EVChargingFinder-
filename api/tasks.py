from celery import shared_task
from .models import StationUsage

@shared_task
def log_usage(station_id, energy):
    StationUsage.objects.create(station_id=station_id, energy_dispensed_kwh=energy)