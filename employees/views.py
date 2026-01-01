from rest_framework import generics
from django.shortcuts import render, redirect
from .models import employeeModel
from .Serializer import EmployeeSerializer
from .forms import EmployeeForm

class EmployeeListCreateAPI(generics.ListCreateAPIView):
    queryset = employeeModel.objects.all()
    serializer_class = EmployeeSerializer

def employee_page(request):
    return render(request,'employee.html')

def employee_page(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees_page')
    else:
        form = EmployeeForm()

    employees = employeeModel.objects.all()
    return render(request, 'employees/employee.html', {'form': form, 'employees': employees})


# Create your views here.
