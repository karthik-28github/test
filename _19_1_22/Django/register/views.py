from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def princi(request):
    if request.methods=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=User.objects.

    return render(request,"princi.html")
