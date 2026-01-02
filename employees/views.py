from rest_framework import generics
from django.shortcuts import render, redirect,get_object_or_404
from .models import employeeModel
from .Serializer import EmployeeSerializer
from .forms import EmployeeForm
from django.http import HttpResponse


# DRF API
class EmployeeListCreateAPI(generics.ListCreateAPIView):
    queryset = employeeModel.objects.all()
    serializer_class = EmployeeSerializer


# READ
def employee_list(request):
    employees = employeeModel.objects.all()
    return render(request, 'employee/employee_list.html', {'employees': employees})

# def employee_list(request):
    # return HttpResponse("EMPLOYEE PAGE WORKING")

# CREATE
def employee_create(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employee/employee_form.html', {'form': form})

# UPDATE
def employee_update(request, id):
    employee = get_object_or_404(employeeModel, id=id)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employee/employee_form.html', {'form': form})

# DELETE
def employee_delete(request, id):
    employee = get_object_or_404(employeeModel, id=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employee/employee_confirm_delete.html', {'employee': employee})



# Create your views here.
