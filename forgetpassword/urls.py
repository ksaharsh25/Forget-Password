from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('register',register,name="Register"),
    path('login',login,name="login"),
    path('forgetpassword',forgetpassword,name="forgetpassword"),
    path('change-password/<token>',password_reset,name="password_reset"),
]