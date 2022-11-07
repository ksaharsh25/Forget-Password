from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('register',register,name="Register"),
    path('login',login,name="login"),
    path('password-reset',register,name="password-reset"),
]