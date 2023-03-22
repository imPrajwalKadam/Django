from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data = {
        'title':"Home Page",
        'heading':"Jay Ganesh",
        'clist':['php','java','zend','android','flutter']
    }
    return render(request,"index.html",data)

def aboutUs(request):
    return HttpResponse('About us')

def course(request):
    return HttpResponse("course function")

def coursedetails(request,courseid):
    return HttpResponse(courseid)
