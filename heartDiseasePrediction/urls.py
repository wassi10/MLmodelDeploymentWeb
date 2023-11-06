from django.urls import path
from . import views

urlpatterns = [
    path('', views.Welcome, name='homepage'),
    path('dashboard', views.Dashboard , name='dashboard')
]
