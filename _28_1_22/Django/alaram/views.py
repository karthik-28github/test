from django.shortcuts import render
from .models import Alaram
import time
import winsound

import datetime
# Create your views here.
def home(request):
    all=Alaram.objects.all()
    if request.method=="POST":
        set1=request.POST.get("set")

        if set1:
            HH=request.POST.get("HH")
            MM=request.POST.get("MM")
            a=Alaram()
            a.HH=HH
            a.MM=MM
            a.save()
            while True:
                date = datetime.datetime.now()
                h = int(date.strftime("%H"))
                m = int(date.strftime("%M"))
                for i in all:
                    if i.HH == h and i.MM==m:
                        print("alaram")
                        winsound.PlaySound("beep.wav", winsound.SND_ASYNC)
                        return render(request,"ontime.html")
        return render(request,"home.html",{"all":all})

    return render(request,"home.html")