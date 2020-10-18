from django.urls import path

from . import views

app_name = 'tracker'

urlpatterns = [
        path('', views.index),
        path('map.html', views.map, name='map'),
        path('sightings.html', views.sightings, name='sightings'),
        path('sightings/add', views.add, name='add'),
        path('sightings/stats', views.stats, name='stats'),
]
