from django.urls import path
from . import views

urlpatterns = [path('',views.index),
               path('weather/',views.sensor_readings),
               path('temp/',views.stream_temp),
               path('hum/',views.stream_hum),
               path('esp/',views.esp),
               ]


