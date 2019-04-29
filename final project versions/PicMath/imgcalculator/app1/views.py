from django.shortcuts import render
from django.http import HttpResponse
#from labreport import dbconnection
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
    return render(request,"index.html",{})
    
def mainpage(request):
    return render(request,"mainpage.html",{})

def upload(request):    
    if request.method=='POST':
        myfile=request.FILES['up']
        fs=FileSystemStorage()
        filename=fs.save("/home/silpa/Desktop/PicMath/imgcalculator/app1/static/userpic/"+myfile.name,myfile)
        print(filename)
        return HttpResponseRedirect("http://127.0.0.1:8000/upload")
    #return render(request,"upload.html",{})
    return render(request,"upload.html",{})