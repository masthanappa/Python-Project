from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Contact2

# Create your views here.
def fun(request):
    return HttpResponse("Hello from Django")
def fun2(request):
    return HttpResponse("Hello from manu")
# def fun3(request):
#     return HttpResponse("Hello froom vidya ")
# def  pro(request):
#     return HttpResponse("Hello to django project")
def home(request):
    return render(request,"home.html")
def  success(request):
   name=request.GET['user']
   return HttpResponse("Wellcome {}".format(name))
def  home2(request):
    if request.method=="POST":
        name2=request.POST.get('name2')
        home2=Contact2(name2=name2)
        home2.save()
    return render(request,"home2.html")
