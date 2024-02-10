from re import template
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

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


    path('password-reset', auth_views.PasswordChangeView.as_view(template_name='password_reset.html'), name='password-reset'),

    path('password-reset-done', auth_views.PasswordChangeDoneView.as_view(template_name='password_reset_done.html'), name='password-reset-done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password-reset-confirm'),

    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html') , name='password-reset-complete'),

]
