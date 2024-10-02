from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def locations(request):
    all_locations = models.MiningLocations.objects.all()
    return render(request, 'locations.html', {'locations': all_locations})