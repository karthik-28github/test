from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,"home.html")
def register(request):
    if request.method=="POST":
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        password=request.POST.get("password")
        mobilenumber=request.POST.get("mobilenumber")
        confirmpassword=request.POST.get("confirmpassword")
        data={"first_name":firstname,"last_name":lastname,"password":password,"confirnpassword":confirmpassword,"mobilenumber":mobilenumber}
        return render(request,'view.html',{"data":data})

    else:
        return render(request,"register.html")
def login(request):
    return render(request,"login.html")

def view(request,data):
    pass


#include<stdio.h>
#include<conio.h>
int a=10
cin>>a
cout<<a;