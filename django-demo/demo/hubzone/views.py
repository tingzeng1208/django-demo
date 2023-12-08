from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.ll

users = [
  {
    'id': '1',
    'name': 'John Doe'
  },
  {
    'id': '2',
    'name': 'Jane Doe'
  },
  {
    'id': '3',
    'name': 'Steve Smith'
  }
]

def home(request):
    # return HttpResponse('Home Page')
    return render(request, 'home.html')

def hubzone(request):
    # return HttpResponse('Hubzone Page')
    return render(request, 'hubzone.html', {'users': users})
