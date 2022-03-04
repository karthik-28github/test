from django.shortcuts import render
from django.http import HttpResponse
from google_images_download import google_images_download
# Create your views here.
def home(request):
    if request.method=="POST":
        text=request.POST.get('text')
        limit=request.POST.get('limit')
        print(text,limit)
        response=google_images_download.googleimagesdownload()
        arguments={'keywords':text,'limit':10,'print_urls':False}
        paths=response.download(arguments)
        print("---------------",paths)
    return render(request,"home.html")