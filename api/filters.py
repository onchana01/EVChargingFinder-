from django_filters import rest_framework as filters
from .models import ChargingStation

class ChargingStationFilter(filters.FilterSet):
    city = filters.CharFilter(lookup_expr='iexact')
    power_kw = filters.NumberFilter()
    renewable = filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = ChargingStation
        fields = ['city', 'power_kw', 'renewable']