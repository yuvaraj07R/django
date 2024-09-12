from django.shortcuts import render
from .models import BusTiming

def bus_timings(request):
    timings = BusTiming.objects.all()
    return render(request, 'bustimings/bustimings.html', {'timings': timings})