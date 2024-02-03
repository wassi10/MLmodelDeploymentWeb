# from multiprocessing import context
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout # if we use auth, we don't require this library
from django.contrib.auth.decorators import login_required
import numpy as np
from .forms import Parameters
from .models import HeartData
import joblib


def Welcome(request):
    return render(request, 'index.html')


@login_required(login_url='signin')
# def Dashboard(request):
#     return render(request, 'homepage.html')


def Dashboard(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # Load the machine learning model
            model = joblib.load('D:\\Web\\MLmodelDeploymentWeb\\heartDiseasePrediction\\MLP_model.sav')

            # Extract data from POST request
            age = float(request.POST.get('age'))
            sex = float(request.POST.get('sex'))
            cp = float(request.POST.get('cp'))
            trestbps = float(request.POST.get('trestbps'))
            chol = float(request.POST.get('chol'))
            fbs = float(request.POST.get('fbs'))
            restcg = float(request.POST.get('restecg'))
            thalach = float(request.POST.get('thalach'))
            exang = float(request.POST.get('exang'))
            oldpeak = float(request.POST.get('oldpeak'))
            slope = float(request.POST.get('slope'))
            ca = float(request.POST.get('ca'))
            thal = float(request.POST.get('thal'))

            # Convert data to numpy array for model prediction
            input_data = np.array([
                age, sex, cp, trestbps, chol, fbs, restcg, thalach, exang, oldpeak, slope, ca, thal
            ]).reshape(1, -1)

            # Make prediction
            output1 = model.predict(input_data)

            danger = 'High' if output1 == 1 else 'Low'
            output1 = output1[0]

            # Save data to the database
            prediction_data = HeartData.objects.create(
                age=age,
                sex=sex,
                cp=cp,
                trestbps=trestbps,
                chol=chol,
                fbs=fbs,
                restcg=restcg,
                thalach=thalach,
                exang=exang,
                oldpeak=oldpeak,
                slope=slope,
                ca=ca,
                thal=thal,
                owner = request.user,
                probability = output1
            )
            prediction_data.save()
            # Render result template with prediction output
            return render(request, 'result.html', {'output1': output1, 'danger': danger})

        # Render homepage if request method is not POST
        return render(request, 'homepage.html')

    # Redirect to sign-in page if user is not authenticated
    return redirect('signin')


# def Dashboard(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             # Load the machine learning model
#             model = joblib.load('D:\\Web\\MLmodelDeploymentWeb\\heartDiseasePrediction\\MLP_model.sav')

#             # Extract data from POST request
#             lis = [
#                 float(request.POST.get('age')),
#                 float(request.POST.get('sex')),
#                 float(request.POST.get('cp')),
#                 float(request.POST.get('trestbps')),
#                 float(request.POST.get('chol')),
#                 float(request.POST.get('fbs')),
#                 float(request.POST.get('restecg')),
#                 float(request.POST.get('thalach')),
#                 float(request.POST.get('exang')),
#                 float(request.POST.get('oldpeak')),
#                 float(request.POST.get('slope')),
#                 float(request.POST.get('ca')),
#                 float(request.POST.get('thal'))
#             ]

#             # Convert list to numpy array for model prediction
#             input_data = np.array(lis).reshape(1, -1)

#             # Make prediction
#             output1 = model.predict(input_data)

#             danger = 'high' if output1 == 1 else 'low'
#             output1=output1[0]
#             # Render result template with prediction output
#             return render(request, 'result.html', {'output1': output1, 'danger':danger})

#         # Render homepage if request method is not POST
#         return render(request, 'homepage.html')

#     # Redirect to sign-in page if user is not authenticated
#     return redirect('signin')




def Result(request):
    if request.user.is_authenticated:
        return render(request, 'result.html')
    return redirect('signin')



# report.html
def Report(request):
    if request.user.is_authenticated:
        record_data = HeartData.objects.filter(owner = request.user) #Filter only those data 
        return render(request, 'report.html', {'record_data':record_data})
    return redirect('signin')


# symptoms.html
def Symptoms(request):
    if request.user.is_authenticated:
        return render(request, 'symptoms.html')
    return redirect('signin')

# prevention.html
def Prevention(request):
    if request.user.is_authenticated:
        return render(request, 'prevention.html')
    return redirect('signin')

# Doctor and hospital list Section
def DoctorAndHospital(request):
    if request.user.is_authenticated:
        return render(request, 'doctorHospitalList.html')
    return redirect('signin')
    # return render(request, 'signin.html')



# For the user to SignIn
def SignIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            messages.warning(request,'Invalid Credentials')
            return redirect('signin')   
        
    return render(request, 'signin.html')


#For the user to resister or sign up.
def SignUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username is already taken')
            return redirect('signup')
        
        # Check if email already exists
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email is already registered')
            return redirect('signup')
        
        # Check if passwords match
        elif password1 != password2:
            messages.info(request, 'Passwords do not match')
            return redirect('signup')

        else:
            # Create the user if all validations pass
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            # messages.success(request, f'Account created for {username}. You can now log in!')
            return redirect('signin')

    return render(request, 'signup.html')


def signout(request): # In order to logout from the website
    logout(request)
    return redirect('homepage')







 



# def index(request):
#     context={'a':1}
#     return render(request, 'index.html')

# Create your views here.
