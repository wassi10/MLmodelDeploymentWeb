from django.urls import path
from . import views

urlpatterns = [
    path('', views.Welcome, name='homepage'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('signin', views.SignIn , name='signin'),
    path('signup', views.SignUp , name='signup'),
    path('signout',views.signout , name='signout'),    
    path('dashboard', views.Dashboard , name='dashboard'),    
    path('result', views.Result , name='result'),
    path('report', views.Report , name='report'),
    path('symptoms', views.Symptoms , name='symptoms'),
    path('prevention', views.Prevention , name='prevention'),
    path('DoctorAndHospital', views.DoctorAndHospital , name='DoctorAndHospital'),

    path('forgot', views.Forgot , name='forgot'),
    path('forgot1', views.Forgot1 , name='forgot1'),
    path('forgot2', views.Forgot2 , name='forgot2'),
    path('forgot3', views.Forgot3 , name='forgot3'),
]
