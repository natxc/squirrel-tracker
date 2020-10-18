from django.shortcuts import render
from tracker.models import Squirrel


def index(request):
    return render(request, 'tracker/index.html', {})

def map(request):
    squirrels = Squirrel.objects.all()[:100]
    context = {'squirrels':squirrels}
    return render(request, 'tracker/map.html', context)
