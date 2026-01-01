from rest_framework import serializers
from .models import employeeModel

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employeeModel
        fields = '__all__'
