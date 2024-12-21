from django.shortcuts import render

# Create your views here.
def myfunction(request):
    return render(request, "index.html", {'name': 'madhurya'})
