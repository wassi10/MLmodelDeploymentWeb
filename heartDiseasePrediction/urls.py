from django.urls import path
from . import views

urlpatterns = [
    path('', views.Welcome, name='homepage'),
    path('dashboard', views.Dashboard , name='dashboard'),
    path('signin', views.SignIn , name='signin'),
    path('signup', views.SignUp , name='signup'),
    path('symptoms', views.Symptoms , name='symptoms'),
    path('prevention', views.Prevention , name='prevention'),
    path('DoctorAndHospital', views.DoctorAndHospital , name='DoctorAndHospital'),
]
