

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('properties/', views.properties, name='properties'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('property-single/<str:pk>', views.property_single, name='property-single'),
    path('agents/', views.agents, name='agents')
    
]