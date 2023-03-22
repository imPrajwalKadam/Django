from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data = {
        'title':"Home Page",
        'heading':"Jay Ganesh",
        'clist':['php','java','zend','android','flutter'],
        'number':[],
        'student_details':[
        {'name':"atharva",'phone':"7020943079"},
        {'name':"viraj",'phone':"9699680306"}
        ]
    }
    return render(request,"index.html",data)

def aboutUs(request):
    return HttpResponse('About us')

def course(request):
    return HttpResponse("course function")

def coursedetails(request,courseid):
    return HttpResponse(courseid)
