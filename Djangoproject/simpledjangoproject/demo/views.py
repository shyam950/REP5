from django.shortcuts import render


# Create your views here.
def myfunction(request):
    return render(request, "index.html", {'name': 'madhurya'})


def add(request):
    x =int(request.GET['num1'])
    y =int(request.GET['num2'])
    result=x+y
    return render(request,"response.html",{'result':result})


