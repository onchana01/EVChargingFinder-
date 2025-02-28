from django.urls import path
from . import views

urlpatterns = [
    path('stations/', views.station_list, name='station_list'),
    path('stations/<int:station_id>/', views.station_detail, name='station_detail'),
    path('reservations/', views.reserve_station, name='reserve_station'),
    path('operator/dashboard/', views.operator_dashboard, name='operator_dashboard'),
    path('operator/stations/<int:station_id>/', views.update_station, name='update_station'),
]