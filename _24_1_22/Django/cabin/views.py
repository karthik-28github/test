import datetime

from django.db import connection
from django.shortcuts import render,redirect
from django.http import HttpResponse
from mysql import connector
import time
# Create your views here.

mycurser=connection.cursor()



name1=''
mob1=0
startime = datetime.datetime.now()
def home(request):
    global name1,mob1
    global name,mob

    if request.method=="POST":
        name = request.POST.get("name")
        if name==None:
            pass
        else:
            name1+=name+" "

        mob = request.POST.get("mob")
        if name==None:
            pass
        else:
            mob1=mob1+int(mob)+1



        if request.method == "POST":
            exit=request.POST.get("exit")
            if exit:
                endtime = datetime.datetime.now()
                totaltime = endtime - startime
                print("--------------", name1, mob1, startime, endtime, totaltime)
                query = "insert into cabin_cabin (name,mob,start,end,total) values (%s,%s,%s,%s,%s)"
                data = (name1, mob1, startime, endtime, totaltime)
                mycurser.execute(query, data)



                return render(request, "ouside.html",
                              {"starttime": startime, "endtime": endtime, "totaltime": totaltime})




            context={"name":name,"mob":mob,"starttime":startime}

        return render(request,"inside.html",context=context)

    return render(request,"home.html")



def display(request):
    # if request.method == "POST":
    #     display = request.POST.get("display")
    #     if display:
    #         query = "select * from cabin_cabin"
    #         val = mycurser.execute(query)
    #         print("------", val)
    #         return render(request, "display.html")
    query = "select name,mob from cabin_cabin"
    val=""
    val =val+str( mycurser.execute(query))
    print("------", val)
    return render(request,"display.html",{"val":val})