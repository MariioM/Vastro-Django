from django.shortcuts import render
from django.urls import reverse_lazy
from . import models
from django.views import generic

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def locations(request):
    all_locations = models.MiningLocations.objects.all()
    return render(request, 'locations.html', {'locations': all_locations})

class LocationsDetailView(generic.DetailView):
    template_name = "location_detail.html"
    model = models.MiningLocations
    context_object_name = 'location'

class LocationCreateView(generic.CreateView):
    model = models.MiningLocations
    template_name = "location_form.html"
    fields = ['name', 'system', 'mineral']

class LocationUpdateView(generic.UpdateView):
    model = models.MiningLocations
    template_name = "location_form.html"
    fields = ['name', 'system', 'mineral']

class LocationDeleteView(generic.DeleteView):
    model = models.MiningLocations
    template_name = 'location_confirm_delete.html'
    success_url = reverse_lazy('locations')