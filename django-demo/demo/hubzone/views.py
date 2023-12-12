from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from . models import *
from . serializer import *
from rest_framework.response import Response

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
  
class EmployeeView(APIView):

    serializer_class = EmployeeSerializer

    def get(self, request):
        output = [{"first_name": output.first_name, "last_name": output.last_name, "email": output.email, "firm": output.firm.name}
                  for output in Employee.objects.all()]
        return Response(output)

    def post(self, request):

        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
          
class FirmView(APIView):
      
      serializer_class = FirmSerializer
  
      def get(self, request):
          output = [{"name": output.name, "address": output.address, "city": output.city, "state": output.state, "zipcode": output.zipcode, "contact": output.contact, "ein": output.ein}
                    for output in Firm.objects.all()]
          return Response(output)
  
      def post(self, request):
  
          serializer = FirmSerializer(data=request.data)
          if serializer.is_valid(raise_exception=True):
              serializer.save()
              return Response(serializer.data)

