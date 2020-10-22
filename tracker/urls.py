from django.urls import path

from . import views

app_name = 'tracker'

urlpatterns = [
            ('', views.index),
            ('map.html', views.map, name='map'),
            ('sightings.html', views.sightings, name='sightings'),
            ('sightings/add', views.add, name='add'),
            ('stats.html', views.stats, name='stats'),
            ('<squirrel_id>/', views.update, name='update'),
            ]


