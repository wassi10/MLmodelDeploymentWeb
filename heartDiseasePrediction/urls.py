from django.urls import path
from . import views

urlpatterns = [
    path('', views.Welcome, name='homepage'),
    path('dashboard', views.Dashboard , name='dashboard'),
    path('DoctorAndHospital', views.DoctorAndHospital , name='DoctorAndHospital'),
    path('symptoms', views.Symptoms , name='symptoms'),
    path('prevention', views.Prevention , name='prevention'),
]
