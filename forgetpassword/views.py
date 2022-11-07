from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from .helpers import send_forget_password_mail
from django.contrib import messages
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
import uuid
def password_reset(request,token):
    context={}
    try:
        profile=Email.objects.get(forget_password_token=token)
        print(profile)
    except Exception as e:
        print(e) 
    
    return render(request,"change-password.html")
def forgetpassword(request):
    if request.method == "POST":
        email=request.POST['email']

        if not Email.objects.filter(email=email):
            messages.success(request,'No user found!')
            return redirect('forgetpassword')
        else:
            user_obj=Email.objects.get(email=email)
            token=str(uuid.uuid4())
            send_forget_password_mail(user_obj,token)
            messages.success(request,'An email is sent')    
            return redirect('forgetpassword')
    return render(request,"forget-password.html")    


