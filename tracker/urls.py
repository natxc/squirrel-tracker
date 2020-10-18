from django.urls import path

from . import views

app_name = 'tracker'

urlpatterns = [
        path('', views.index),
        path('map', views.map, name='map'),
]
