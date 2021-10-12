from django.urls import path
from . import views

urlpatterns = [path('',views.get_name1),
               path('name_json/',views.get_name_json),
               ]


