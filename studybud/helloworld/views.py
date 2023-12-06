from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.

def testfunction():
    x=1
    y=10

def hello(request):
    testfunction()
    return HttpResponse("hello world")

def hello_html(request):
    return render(request, 'helloworld.html')

def hello_var(request):
    return render(request, 'helloworld_variable.html', {'name': 'Ting Zeng'})
