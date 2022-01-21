from django.shortcuts import render
context={}
# Create your views here.
def build(request):
    global context

    if request.method=="POST":
        firstname=request.POST.get("firstname")
        secondname=request.POST.get("secondname")
        fathername=request.POST.get("fathername")
        email=request.POST.get("email")
        permanentaddress=request.POST.get("permanentaddress")
        country=request.POST.get("country")
        city=request.POST.get("city")
        zip=request.POST.get("zip")
        certification=request.POST.get("certification")
        skillset=request.POST.get("skillset")
        project=request.POST.get("project")
        schoolname=request.POST.get("schoolname")
        sslcs=request.POST.get("sslcs")
        sslce=request.POST.get("sslce")
        pucollege=request.POST.get("collegename")
        pucs=request.POST.get("pucs")
        puce=request.POST.get("puce")
        degreecollege=request.POST.get("degreecollege")
        degrees=request.POST.get("degrees")
        degreee=request.POST.get("degreee")
        DOB=request.POST.get("DOB")
        data=[firstname,secondname,fathername,email,permanentaddress,country,city,zip,
              certification,skillset,project,schoolname,sslce,sslcs,pucollege,pucs,puce,
              degreecollege,degrees,degreee,DOB]
        context={'firstname':firstname,'secondname':secondname,'fathername':fathername,
                 'email':email,'permanentaddress':permanentaddress,'country':country,
                 'city':city,'zip':zip,'certification':certification,'skillset':skillset,
                 'project':project,'schoolname':schoolname,'sslce':sslce,'sslcs':sslcs,
                 'pucollege':pucollege,'pucs':pucs,'puce':puce,'degreecollege':degreecollege,
                 'degrees':degrees,'degreee':degreee,'DOB':DOB}

        return render(request,"display.html",context=context)
    else:
        return render(request,"build.html")


def download(request):
    global context
    if request.method=="POST":
        d=request.POST.get("download")
        if d:
            with open("resume.pdf","x") as f:
                f.write(context)
    else:
        return render(request,"display.html")
