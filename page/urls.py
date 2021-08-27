from django.urls import path
from . import views

urlpatterns = [path('',views.get_name1),
               path('stream/',views.stream),
               path('name/',views.get_name),
               ]


