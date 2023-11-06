# from multiprocessing import context
from django.shortcuts import render

def Welcome(request):
    return render(request, 'index.html')

def Dashboard(request):
    return render(request, 'homepage.html')

# Doctor and hospital list Section
def DoctorAndHospital(request):
    return render(request, 'doctorHospitalList.html')

# symptoms.html
def Symptoms(request):
    return render(request, 'symptoms.html')

# prevention.html
def Prevention(request):
    return render(request, 'prevention.html')


















# def index(request):
#     context={'a':1}
#     return render(request, 'index.html')

# Create your views here.
