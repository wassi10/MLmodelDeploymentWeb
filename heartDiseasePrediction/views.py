# from multiprocessing import context
from email.message import EmailMessage
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout, get_user_model # if we use auth, we don't require this library
from django.contrib.auth.decorators import login_required
import numpy as np
from .models import HeartData
import joblib #model import
import re #regex

# Email verification
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string

# from django.contrib.auth import get_user_model
# from django.utils.encoding import force_text
# from django.utils.encoding import smart_text

from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode




def Welcome(request):
    if request.user.is_authenticated:
        return render(request, 'homepage.html')
    return render(request, 'index.html')


@login_required(login_url='signin')

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
            # input_data = np.array([
            #     age, sex, cp, trestbps, chol, fbs, restcg, thalach, exang, oldpeak, slope, ca, thal
            # ]).reshape(1, -1)

            # # Make prediction
            # output1 = model.predict(input_data)


            # Make prediction
            probabilities = model.predict_proba(np.array([age,sex,cp,trestbps,chol,fbs,restcg,thalach,exang,oldpeak,slope,ca,thal]).reshape(1,-1))

            probability_of_heart_disease = probabilities[0][1] * 100
            probability_formatted = "{:.4f}".format(probability_of_heart_disease)
            
            
            danger = 'High' if probability_of_heart_disease >= 50 else 'Low'
            

            # Save data to the database
            prediction_data = HeartData(
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
                probability = probability_formatted
            )
            prediction_data.save()
            # Render result template with prediction output
            return render(request, 'result.html', {'output1': probability_formatted, 'danger': danger})

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
#             age = float(request.POST.get('age'))
#             sex = float(request.POST.get('sex'))
#             cp = float(request.POST.get('cp'))
#             trestbps = float(request.POST.get('trestbps'))
#             chol = float(request.POST.get('chol'))
#             fbs = float(request.POST.get('fbs'))
#             restcg = float(request.POST.get('restecg'))
#             thalach = float(request.POST.get('thalach'))
#             exang = float(request.POST.get('exang'))
#             oldpeak = float(request.POST.get('oldpeak'))
#             slope = float(request.POST.get('slope'))
#             ca = float(request.POST.get('ca'))
#             thal = float(request.POST.get('thal'))

#             # Convert data to numpy array for model prediction
#             # input_data = np.array([
#             #     age, sex, cp, trestbps, chol, fbs, restcg, thalach, exang, oldpeak, slope, ca, thal
#             # ]).reshape(1, -1)

#             # # Make prediction
#             # output1 = model.predict(input_data)

#             output1 = model.predict(np.array([age,sex,cp,trestbps,chol,fbs,restcg,thalach,exang,oldpeak,slope,ca,thal]).reshape(1,-1))

#             danger = 'High' if output1 == 1 else 'Low'
#             output1 = output1[0]

#             # Save data to the database
#             prediction_data = HeartData(
#                 age=age,
#                 sex=sex,
#                 cp=cp,
#                 trestbps=trestbps,
#                 chol=chol,
#                 fbs=fbs,
#                 restcg=restcg,
#                 thalach=thalach,
#                 exang=exang,
#                 oldpeak=oldpeak,
#                 slope=slope,
#                 ca=ca,
#                 thal=thal,
#                 owner = request.user,
#                 probability = output1
#             )
#             prediction_data.save()
#             # Render result template with prediction output
#             return render(request, 'result.html', {'output1': output1, 'danger': danger})

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
            messages.warning(request,'Username or Password not match.')
            return redirect('signin')   
        
    return render(request, 'signin.html')



# UserModel = get_user_model()
User = get_user_model()
def activate(request, uidb64, token):
    
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        # Activate the user account
        user.is_active = True
        user.save()
        messages.info(request, 'Your account has been activated.')
        return redirect('signin')  
    else:
        messages.info(request, 'Activation link is invalid.')
        return redirect('signup')  


#For the user to resister or sign up.
# username regex pattern '^[a-zA-Z0-9_]*$': myUsername, user123, user_name, User123_.username123

def SignUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Define regex patterns for validation
        username_pattern = '^[a-zA-Z0-9_]*$'
        email_pattern = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        password_pattern = '(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$'

        # Check username format
        if not re.match(username_pattern, username):
            messages.info(request, 'Username must contain only letters, numbers, and underscores.')
            return redirect('signup')
        
        # Check email format
        elif not re.match(email_pattern, email):
            messages.info(request, 'Invalid email format')
            return redirect('signup')
        
        # Check password format
        elif not re.match(password_pattern, password1):
            messages.info(request, 'Password must be at least 8 characters with 1 digit, 1 lowercase, and 1 uppercase.')
            return redirect('signup')

        # Check if username already exists
        elif User.objects.filter(username=username).exists():
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
            user.is_active = False  # Mark the user as inactive until email verification
            user.save()

            # Send verification email
            current_site = get_current_site(request)
            mail_subject = 'Account Verification'
            message = render_to_string('email_verification.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            # send_mail = email
            # to_email = EmailMessage(mail_subject, message, to=[send_mail])
            # to_email.send()

            to_email = email
            send_mail(mail_subject, message,'HDPS', [to_email])
            messages.info(request, 'A verification email has been sent.')


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
