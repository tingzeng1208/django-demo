from rest_framework import serializers
from . models import *


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'firm']
        
class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = ['name', 'address', 'city', 'state', 'zipcode', 'contact', 'ein']
    
    def create(self, validated_data):
        firm_name = validated_data.pop('firm_name', None)
        firm = None
        if firm_name:
            firm = Firm.objects.get(name=firm_name)
            # You may want to handle the case where the firm doesn't exist.
        employee = Employee.objects.create(**validated_data, firm=firm)
        return employee