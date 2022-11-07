from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
# Create your views here.
def register(request):
    if  request.method =="POST":
        email=request.POST['email']
        password=request.POST['password']

        database=Email(email=email,password=password)
        database.save()
        return redirect('login')
    return render(request,'register.html')

def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        admin=Email.objects.filter(email=email,password=password)


        if admin.exists():
            return HttpResponse("Done")

        else:
            return HttpResponse("Foget password") 

    return render(request,"login.html")               

def password_reset(request):

    return render(request,"forget-password.html")    