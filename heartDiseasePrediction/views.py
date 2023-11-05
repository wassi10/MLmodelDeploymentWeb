# from multiprocessing import context
from django.shortcuts import render

def Welcome(request):
    return render(request, 'index.html')
























# def index(request):
#     context={'a':1}
#     return render(request, 'index.html')

# Create your views here.
