from django.shortcuts import render

# Create your views here.


def home(request):
    if request.method=="POST":
        mobileno=request.POST.get("mobileno")
        otp=request.POST.gt("otp")
