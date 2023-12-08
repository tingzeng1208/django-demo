from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.ll

def home(request):
    # return HttpResponse('Home Page')
    return render(request, 'home.html')

def hubzone(request):
    # return HttpResponse('Hubzone Page')
    return render(request, 'hubzone.html')
