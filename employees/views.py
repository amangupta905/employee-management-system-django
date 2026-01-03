from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import employeeModel
from .forms import EmployeeForm
from django.core.paginator import Paginator

@login_required
def employee_list(request):
    employees = employeeModel.objects.all().order_by('id')

    # 🔍 Search
    search_query = request.GET.get('q')
    if search_query:
        employees = employees.filter(
            name__icontains=search_query
        ) | employees.filter(
            email__icontains=search_query
        )

    # Filter by department
    department = request.GET.get('department')
    if department:
        employees = employees.filter(department__icontains=department)

    #  Pagination
    paginator = Paginator(employees, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'employee/employee_list.html',
        {
            'page_obj': page_obj,
            'search_query': search_query,
            'department': department
        }
    )

@login_required
def employee_create(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employee/employee_form.html', {'form': form})

@login_required
def employee_update(request, id):
    employee = get_object_or_404(employeeModel, id=id)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employee/employee_form.html', {'form': form})

@login_required
def employee_delete(request, id):
    employee = get_object_or_404(employeeModel, id=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employee/employee_confirm_delete.html', {'employee': employee})
