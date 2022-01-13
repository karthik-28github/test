from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Registration
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request,"home.html")
def register(request):
    if request.method=="POST":
        email=request.POST.get("email")
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        mobilenumber = request.POST.get("mobilenumber")
        password=request.POST.get("password")
        confirmpassword=request.POST.get("confirmpassword")

        if password==confirmpassword:
            if Registration.objects.get(email!=email:
                registration=Registration(firstname=firstname, lastname=lastname, mobilenumber=mobilenumber, password=password,
                             confirmpassword=confirmpassword)
                registration.save()
                data={'name':'abhi'}
                return render(request,'view.html',data=data)
        #     else:
        #         print("emaiil exists")
        #         # messages.warning(request,"the email alredy exists")
        #         # return redirect("home")
        #
        # else:
        #     print("pass not same")
        #     #return messages.warning(request, "the password does not match")
        #
        # data={"email":email,"first_name":firstname,"last_name":lastname,"password":password,"confirnpassword":confirmpassword,"mobilenumber":mobilenumber}
        # return render(request,'view.html',{"data":data})
        # # return 'YES'

    else:
        return render(request,"register.html")
def login(request):
    return render(request,"login.html")

def view(request,data):
    pass
