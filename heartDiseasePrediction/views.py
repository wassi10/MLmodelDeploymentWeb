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


# def Dashboard(request):
#     # Direct authenticated users to the home page
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = Parameters(request.POST)
#             if form.is_valid():
#                 # Extract cleaned data from the form
#                 age = form.cleaned_data['age']
#                 sex = form.cleaned_data['sex']
#                 cp = form.cleaned_data['cp']
#                 trestbps = form.cleaned_data['trestbps']
#                 chol = form.cleaned_data['chol']
#                 fbs = form.cleaned_data['fbs']
#                 restcg = form.cleaned_data['restecg']
#                 thalach = form.cleaned_data['thalach']
#                 exang = form.cleaned_data['exang']
#                 oldpeak = form.cleaned_data['oldpeak']
#                 slope = form.cleaned_data['slope']
#                 ca = form.cleaned_data['ca']
#                 thal = form.cleaned_data['thal']

#                 # Load the model
#                 try:
#                     cls = joblib.load('XGBoost_model.sav')
#                     # Make predictions
#                     output, output1 = cls.predict(np.array([age, sex, cp, trestbps, chol, fbs, restcg, thalach, exang, oldpeak, slope, ca, thal]).reshape(1, -1))
#                     danger = 'high' if output == 1 else 'low'
#                     output1 = output1[0]
#                     # Save data to database
#                     saved_data = HeartData(age=age, sex=sex, cp=cp, trestbps=trestbps, chol=chol, fbs=fbs, restcg=restcg, thalach=thalach, exang=exang, oldpeak=oldpeak, slope=slope, ca=ca, thal=thal, owner=request.user, probability=output1)
#                     saved_data.save()
#                     return render(request, 'result.html', {'output1': output1, 'danger': danger})
#                 except Exception as e:
#                     # Handle model loading or prediction errors
#                     return render(request, 'error.html', {'error': str(e)})

#         # For GET requests or invalid form submissions
#         form = Parameters()
#         return render(request, 'homepage.html', {'form': form})
#     else:
#         # Redirect non-authenticated users to the signin page
#         return redirect('signin')


def Dashboard(request): #Directs the user to home page . Different for authenticated and non authenticated users.
    if request.user.is_authenticated:
        if request.method=='POST':
    
            form=Parameters(request.POST)
            if form.is_valid():
                age=form.cleaned_data['age']
                sex=form.cleaned_data['sex']
                cp=form.cleaned_data['cp']
                trestbps=form.cleaned_data['trestbps']
                chol=form.cleaned_data['chol']
                fbs=form.cleaned_data['fbs']
                restcg=form.cleaned_data['restecg']
                thalach=form.cleaned_data['thalach']
                exang=form.cleaned_data['exang']
                oldpeak=form.cleaned_data['oldpeak']
                slope=form.cleaned_data['slope']
                ca=form.cleaned_data['ca']
                thal=form.cleaned_data['thal']


                cls = joblib.load('XGBoost_model.sav')
                
                output , output1 = cls.predict(np.array([age,sex,cp,trestbps,chol,fbs,restcg,thalach,exang,oldpeak,slope,ca,thal]).reshape(1,-1))

                danger = 'high' if output == 1 else 'low'
                output1=output1[0]
                saved_data = HeartData(age=age ,  # Saving to database
                sex = sex,
                cp = cp,
                trestbps = trestbps,
                chol = chol,
                fbs = fbs,
                restcg = restcg , 
                thalach = thalach , 
                exang = exang,
                oldpeak = oldpeak,
                slope = slope,
                ca = ca,
                thal = thal,
                owner = request.user,
                probability = output1
                )  #Saved the authenticated users data in the database.
                saved_data.save()
                return render(request , 'result.html',{'output1':output1 , 'danger':danger})


        form = Parameters()
        return render(request , 'homepage.html', {'form':form})
    return redirect('signin')



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
