import logging
logger = logging.getLogger('api')
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import ChargingStation, Reservation, StationUsage
from .serializers import ChargingStationSerializer, ReservationSerializer, StationUsageSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .permissions import IsOperatorOrReadOnly

@api_view(['GET'])
def station_list(request):
    # Query parameters
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')
    radius = request.GET.get('radius', 10)  # Default 10 km
    name = request.GET.get('name')

    if latitude and longitude:
        # Search by coordinates
        user_location = Point(float(longitude), float(latitude), srid=4326)
        stations = ChargingStation.objects.filter(
            location__distance_lte=(user_location, Distance(km=float(radius)))
        )
    elif name:
        # Search by name (case-insensitive partial match)
        stations = ChargingStation.objects.filter(name__icontains=name)
    else:
        # Return all stations if no filters provided
        stations = ChargingStation.objects.all()

    serializer = ChargingStationSerializer(stations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def station_detail(request, station_id):
    station = ChargingStation.objects.get(station_id=station_id)
    serializer = ChargingStationSerializer(station)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def reserve_station(request):
    serializer = ReservationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        station = ChargingStation.objects.get(station_id=serializer.data['station'])
        station.availability = "Occupied"
        station.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsOperatorOrReadOnly])
def operator_dashboard(request):
    stations = ChargingStation.objects.all()
    usage = StationUsage.objects.all()
    serializer = ChargingStationSerializer(stations, many=True)
    usage_serializer = StationUsageSerializer(usage, many=True)
    return Response({
        'stations': serializer.data,
        'usage': usage_serializer.data
    })

@api_view(['POST'])
@permission_classes([IsAdminUser])
def update_station(request, station_id):
    station = ChargingStation.objects.get(station_id=station_id)
    serializer = ChargingStationSerializer(station, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

@api_view(['GET'])
def station_list(request):
    logger.info(f"Station list requested with params: {request.GET}")
    stations = ChargingStation.objects.all()
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')
    radius = request.GET.get('radius', 10)
    name = request.GET.get('name')

    if latitude and longitude:
        user_location = Point(float(longitude), float(latitude), srid=4326)
        stations = stations.filter(location__distance_lte=(user_location, Distance(km=float(radius))))
    elif name:
        stations = stations.filter(name__icontains=name)

    # Apply filters, search, and pagination
    filterset = ChargingStationFilter(request.GET, queryset=stations)
    queryset = filterset.qs
    paginator = StandardResultsSetPagination()
    page = paginator.paginate_queryset(queryset, request)
    serializer = ChargingStationSerializer(page, many=True)
    return paginator.get_paginated_response(serializer.data)