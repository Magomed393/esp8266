from django.urls import path
from . import views

urlpatterns = [path('',views.index),
               path('weather/',views.get_temp),
               path('stream/',views.stream),
               path('name/',views.get_name),
               ]


