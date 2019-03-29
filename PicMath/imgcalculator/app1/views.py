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