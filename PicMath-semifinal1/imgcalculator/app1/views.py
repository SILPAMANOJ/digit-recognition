from django.shortcuts import render
from django.http import HttpResponse
#from labreport import dbconnection
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.files.storage import FileSystemStorage
from app1 import numberrecognition
#import os

# Create your views here.
global imgname
global myfile
def index(request):
    return render(request,"index.html",{})
    
def mainpage(request):
    return render(request,"mainpage.html",{})

def upload(request):
    global imgname
    global myfile
    if request.method=='POST':
        myfile=request.FILES['up']

        fs=FileSystemStorage()
        filename=fs.save("/home/silpa/Desktop/PicMath/imgcalculator/app1/static/userpic/"+myfile.name,myfile)
        imgname=filename
        #print("img",imgname)
        return render(request,'upload.html',{'upimg':myfile})
    return render(request,'upload.html',{})

def result(request):
    global imgname
    global myfile
    print(myfile)
    import os
    import re
    os.system("tesseract "+imgname+" output")
    s=numberrecognition.operate()
    print(s)
    return render(request,'result.html',{'res':s,'eq':myfile})
    #return render(request,"result.html",{})
        