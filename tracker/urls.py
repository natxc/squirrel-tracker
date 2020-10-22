from django.urls import path

from . import views

app_name = 'tracker'

urlpatterns = [
           path('', views.index),
           path('index.html', views.index, name='home'),
           path('map.html', views.map, name='map'),
           path('sightings.html', views.sightings, name='sightings'),
           path('sightings/add', views.add, name='add'),
           path('stats.html', views.stats, name='stats'),
           path('<Unique_Squirrel_ID>/', views.update, name='update'),
            ]


