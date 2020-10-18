from django.shortcuts import render
from tracker.models import Squirrel
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return render(request, 'tracker/index.html', {})

def map(request):
    squirrels = Squirrel.objects.all()[:100]
    context = {
            'squirrels': squirrels
        }
    return render(request, 'tracker/map.html', context)

def sightings(request):
    squirrles = Squirrel.objects.all()
    context = {
            'squirrels': squirrels
            }
    return render(request, 'tracker/sightings.html', context)
