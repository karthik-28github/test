from django.http import HttpResponse
from django.shortcuts import render,redirect
from task.myforms import Register,Login
from task import models
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method=="POST":
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        mobile=request.POST.get("mobile")
        email=request.POST.get("email")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")

        if password1==password2:
            if models.Register.objects.filter(email=email):
                messages.info(request,"Email Already Exists")
                return redirect("register")
            if models.Register.objects.filter(mobile=mobile):
                messages.info(request,"Mobile no Already Exists")
                return redirect("register")
            new_user=models.Register(firstname=firstname,lastname=lastname,
                          mobile=mobile,email=email,password1=password1,
                          password2=password2)
            new_user.save()
            messages.info(request,"successfully Registered ")
            messages.info(request,"Try to login using Credentilas")
            return redirect("login")
        else:
            messages.info(request,"Password does not match")
        return redirect("register")
    temp = {}
    temp["form"] = Register()
    return render(request,"register.html",temp)

def login(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        if models.Register.objects.filter(email=email,password1=password):
            return redirect("home1")
        return redirect("register")
    temp = {}
    temp["form"] = Login()
    return render(request,"login.html",temp)

def home1(request):
    task=models.Tasks.objects.all()
    if request.method=="POST":
        add=request.POST.get("add")
        update=request.POST.get("update")
        delete=request.POST.get("delete")
        if add:
            name=request.POST.get("task1")
            new_task=models.Tasks(name=name)
            new_task.save()
            return redirect("home1")

        if update:
            id=request.POST.get("id1")
            # name=request.POST.get("task2")
            new_task=models.Tasks.objects.filter(id=id).get()
            new_task.name=request.POST.get("task2")
            new_task.save()
            return redirect("home1")

        if delete:
            id=request.POST.get("id2")
            new_task=models.Tasks.objects.filter(id=id).delete()
            task.save()
            return redirect("home1")

    return render(request,"home1.html",{"task":task})