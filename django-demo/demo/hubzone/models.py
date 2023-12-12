from django.db import models


class Firm(models.Model):
  name = models.CharField(max_length=100)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=2)
  zipcode = models.CharField(max_length=10)
  contact = models.CharField(max_length=100)
  ein = models.CharField(max_length=12)
  # Add more fields as needed


class Employee(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.EmailField()
  firm = models.ForeignKey(Firm, on_delete=models.CASCADE)
  # Add more fields as needed
  

  
# class React(models.Model):
#   employee = models.CharField(max_length=30)
#   department = models.CharField(max_length=200)
