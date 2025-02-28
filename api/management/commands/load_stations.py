import json
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
from api.models import ChargingStation

class Command(BaseCommand):
    help = "Load charging stations from JSON"

    def handle(self, *args, **kwargs):
        with open('ev.json', 'r') as f:
            data = json.load(f)
        for station in data:
            ChargingStation.objects.create(
                station_id=station['station_id'],
                name=station['name'],
                city=station['city'],
                location=Point(station['longitude'], station['latitude']),
                power_kw=station['power_kw'],
                connector_types=station['connector_types'],
                price_eur_per_kwh=station['price_eur_per_kwh'],
                availability=station['availability'],
                renewable=station['renewable']
            )
        self.stdout.write(self.style.SUCCESS("Loaded 20 charging stations"))