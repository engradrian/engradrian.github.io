from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "portfolio/homepage.html")

def webpage(request):
    return render(request, "portfolio/webpage.html")

def mywork(request):
    return render(request, "portfolio/mywork.html")