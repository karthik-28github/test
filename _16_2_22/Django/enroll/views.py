from django.http import HttpResponse
from django.shortcuts import render,redirect
from enroll.myforms import Register,RegisterPrincipal,LoginPrincipal
from enroll import models
from django.contrib import messages
# Create your views here.
def registerprincipal(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")
        if password1==password2:
            if models.RegisterPrincipal.objects.filter(email=email):
                messages.error(request,"email is already registered try other")
                return redirect("registerprincipal")

            new_princi=models.RegisterPrincipal(email=email,password1=password1)
            new_princi.save()
            messages.success(request,"succefully registered")
            messages.success(request,"try to login using the credentials")
            return redirect("loginprincipal")
        else:
            messages.error(request,"sorry password doesnt match")
            return redirect("registerprincipal")
    temp = {}
    temp["form"] = RegisterPrincipal()
    return render(request, "registerprincipal.html", temp)

def loginprincipal(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password1=request.POST.get("password1")
        if models.RegisterPrincipal.objects.filter(email=email):
            if models.RegisterPrincipal.objects.filter(email=email,password1=password1):
                return redirect("home")
            else:
                messages.error(request,"please check your email id and password")
                return redirect("loginprincipal")
        else:
            messages.error(request,"you dont have an account please register here")
            return redirect("registerprincipal")
    temp = {}
    temp["form"] = LoginPrincipal()
    return render(request,"loginprincipal.html",temp)
'''
def enroll(request):
    if request.method=="POST":
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        studingin=request.POST.get("studingin")
        blood=request.POST.get("blood")

    temp = {}
    temp["form"] = RegisterPrincipal()
    return render(request,"registerprincipal.html",temp)
'''


def home(request):
    std=models.Register.objects.all()
    if request.method=="POST":
        add=request.POST.get("add")
        update=request.POST.get("update")
        delete=request.POST.get("delete")
        if add:
            firstname=request.POST.get("firstname")
            lastname=request.POST.get("lastname")
            studing=request.POST.get("studing")
            bloodgroup=request.POST.get("bloodgroup")
            new_std=models.Register(firstname=firstname,lastname=lastname,
                                     studing=studing,bloodgroup=bloodgroup)
            new_std.save()
            return redirect("home")

        if update:
            id=request.POST.get("id1")
            new_std=models.Register.objects.filter(id=id).get()
            firstname = request.POST.get("firstname")
            lastname = request.POST.get("lastname")
            blood = request.POST.get("blood")
            if firstname:
                new_std.firstname=firstname
            if lastname:
                new_std.lastname = lastname
            if blood:
                new_std.blood = blood
            new_std.save()
            return redirect("home")

        if delete:
            id=request.POST.get("id2")
            name=models.Register.objects.get()
            new_task=models.Register.objects.filter(id=id).delete()
            messages.success(request,f"student {name.id} {name.firstname } has been successfully deleted ")
            return redirect("home")
    temp = {}
    temp["form"] = Register()
    temp["std"]=std
    return render(request, "home.html", temp)