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
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels': squirrels
            }
    return render(request, 'tracker/sightings.html', context)

def add(request):
    if request.method =="POST":
        form = SquirrelAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tracker:sightings')
        else: 
            form = SquirrelAddForm()
        context = {
                'form': form
                 }
        return render(request, 'tracker/add.html', context)

def stats(request): 
    total_seen = Squirrel.objects.all().count()
    adults_seen = Squirrel.objects.filter(age='Adult').count()
    juvenile_seen = Squirrel.objects.filter(age='Juvenile').count()
    number_running = Squirrel.objects.filter(running=True).count()
    number_climbing = Squirrel.objects.filter(climbing=True).count()
    context = {
            'total_seen': total_seen,
            'adults_seen': adults_seen,
            'juvenile_seen': juvenile_seen,
            'number_running': number_running,
            'number_climbing': number_climbing,
            }
    return render(request, 'tracker/stats.html', context)

