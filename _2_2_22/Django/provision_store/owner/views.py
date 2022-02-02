from django.shortcuts import render, HttpResponse, redirect
from .models import Credential,Item
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def home(request):
    item1=Item.objects.all()

    if request.method=="POST":
        name=request.POST.get("name")
        price=request.POST.get("price")
        quantity=request.POST.get("quantity")

        add=request.POST.get("add")

        id=request.POST.get("id")
        delete=request.POST.get("delete")

        update=request.POST.get("update")
        if add:
            item=Item()
            item.name=name
            item.price=price
            item.quantity=quantity
            item.save()
            return redirect("home")

        if delete:
            item2=Item.objects.filter(id=id)
            item2.delete()
            return redirect("home")

        if update:
            item3=Item.objects.get(name=name)
            if item3:
                item3.price=price
                item3.quantity=item3.quantity+float(quantity)
                item3.save()
                print(item3)
                return  redirect("home")
    else:
        return render(request,"home.html",{"item":item1})

def register(request):
    if request.method=="POST":
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirmpassword=request.POST.get("confirmpassword")

        login=request.POST.get("login")
        if login:
            return redirect("login")

        if password==confirmpassword:
            user=Credential.objects.filter(email=email).first()
            try :
                if not user:

                    new_user=Credential(firstname=firstname,lastname=lastname,email=email,password=password)
                    new_user.save()
                    context={"data":"------successfully registered Try to login"}
                    return render(request,"login.html",context)

                else:
                    messages.error(request,"Email already Registered")
            except:
                messages.error(request,"problem in try block")

        else:
            messages.error(request,"password does not match")
    return render(request,"register.html")

def login(request,context=None):


    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        register=request.POST.get("register")

        if register:
            return redirect("register")

        user=Credential.objects.filter(email=email,password=password).all

        if user:
            return redirect("home")

    return render(request,"login.html",context)

def logout(request):

    return render(request,"logout.html")

def display(request):
    return HttpResponse("welome to django")