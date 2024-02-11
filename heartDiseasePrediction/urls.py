from re import template
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Welcome, name='homepage'),
    path('analysis', views.Analysis , name='analysis'),
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

    # pass: Hello1@23

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='reset_password'),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='reset_password_sent.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),

    path('reset_password_complete>/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),


    # path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),


    # path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    # path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),

    # path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),


    # path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

]
