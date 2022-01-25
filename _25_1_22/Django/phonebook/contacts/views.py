from django.http import request
from django.shortcuts import render,redirect
from .models import Contact

# Create your views here.
def home(request):
    if request.method=="POST":
        add=request.POST.get("add")
        display=request.POST.get("display")
        remove=request.POST.get("remove")
        if add:
            return redirect("add")
        if remove:
            return redirect("remove")
        if display:
            return redirect("display")
    return render(request,"home.html")

def add(request):
    c=Contact.objects.all()

    if request.method=="POST":
        name=request.POST.get("name")
        phoneno=request.POST.get("phoneno")
        email=request.POST.get("email")
        val={"name":name,"phoneno":phoneno,"email":email}
        c1=Contact()
        c1.name=name
        c1.phoneno=phoneno
        c1.email=email
        c1.save()

        return render(request, "display.html",{"c":c})

    return render(request,"add.html")

def remove(request):
    c = Contact.objects.all()
    if request.method=="POST":
        delphone=request.POST.get("delphone")
        q=Contact.objects.filter(phoneno=delphone)
        q.delete()

        return render(request, "remove.html", {"c": c})
        # c.delete(delphone)



    return render(request,"remove.html",{"c":c})


def display(request):
    c=Contact.objects.all()

    return render(request,"display.html",{"c":c})
