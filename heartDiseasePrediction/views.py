# from multiprocessing import context
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


def Welcome(request):
    return render(request, 'index.html')

def Dashboard(request):
    return render(request, 'homepage.html')

# SignIn
def SignIn(request):
    return render(request, 'signin.html')

# SignUp
def SignUp(request):
    return render(request, 'signup.html')

# symptoms.html
def Symptoms(request):
    return render(request, 'symptoms.html')

# prevention.html
def Prevention(request):
    return render(request, 'prevention.html')

# Doctor and hospital list Section
def DoctorAndHospital(request):
    return render(request, 'doctorHospitalList.html')


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










 























# def signup(request): #For the user to resister or sign up.

    # if request.method == 'POST':
    #     first_name = request.POST['first_name']
    #     last_name = request.POST['last_name']
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     email = request.POST['email']

        
    #     if User.objects.filter(username=username).exists():
    #         messages.info(request,'Username taken')
    #         return redirect('signup')
    #     elif User.objects.filter(email=email).exists():
    #         messages.info(request,'Email taken')
    #         return redirect('signup')
    #     else:
    #         user = User.objects.create_user(username=username, password=password,email=email,first_name = first_name,last_name=last_name)
            
    #         user.save()
            
    #         messages.success(request,f"User {username} created!")
    #         return redirect('signin')
    #     #return redirect('/')
    # else:   
#         return render(request,'signup.html')


# def signout(request): # In order to logout from the website
#     auth.logout(request)
#     return redirect('/')














# def index(request):
#     context={'a':1}
#     return render(request, 'index.html')

# Create your views here.
