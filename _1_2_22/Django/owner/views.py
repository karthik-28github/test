from django.shortcuts import render, HttpResponse, redirect
from .models import Credential,Item
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method=="POST":
        register=request.POST.get("register")
        login=request.POST.get("login")
        logout=request.POST.get("logout")

        if register:
            return render("register")
        if login:
            return render("login")
        if logout:
            return render("logout")

    return render(request,"home.html")

def register(request):
    if request.method=="POST":
        firstname=request.POST.get("register")
        lastname=request.POST.get("lastname")
        email=request.POST.get("email")
        password=request.POST.get("password")

        confirmpassword=request.POST.get("confirmpassword")
        if password==confirmpassword:
            user=Credential.objects.all()
            if email==user.email:
                messages.error(request,"Email already Registered")
            else:
                new_user=Credential(firstname=firstname,lastname=lastname,email=email,password=password)
        else:
            messages.error(request,"password does not match")
    return render(request,"register.html")

def login(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
    return render(request,"login.html")

def logout(request):

    return render(request,"logout.html")

def display(request):
    return HttpResponse("welome to django")