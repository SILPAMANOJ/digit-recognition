from django.shortcuts import render
from django.http import HttpResponse
#from labreport import dbconnection
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.files.storage import FileSystemStorage
from app1 import numberrecognition
#import os

# Create your views here.
imgname="h"
def index(request):
    return render(request,"index.html",{})
    
def mainpage(request):
    return render(request,"mainpage.html",{})
def result(request):
    return render(request,"result.html",{})

def upload(request):
    global imgname
    if request.method=='POST':
        myfile=request.FILES['up']

        fs=FileSystemStorage()
        filename=fs.save("/home/silpa/Desktop/PicMath/imgcalculator/app1/static/userpic/"+myfile.name,myfile)
        imgname=filename
        #print("img",imgname)
        return render(request,'upload.html',{'upimg':myfile})
    if request.method=='GET':
        import os
        import re
        os.system("tesseract "+imgname+" output")
        s=numberrecognition.operate()
        print(s)
        #return render(request,'upload.html',{'res':s})
    return render(request,'upload.html',{})


        