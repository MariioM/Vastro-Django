from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('locations', views.locations, name='locations'),
    path('location/<int:pk>', views.LocationsDetailView.as_view(), name='location_detail'),
    path('locations/add', views.LocationCreateView.as_view(), name='location_form'),
    path('location/<int:pk>/update', views.LocationUpdateView.as_view(), name='location_form'),
    path('location/<int:pk>/delete', views.LocationDeleteView.as_view(), name='location_confirm_delete'),
]