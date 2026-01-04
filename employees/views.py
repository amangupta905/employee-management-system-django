from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import employeeModel
from .forms import EmployeeForm
from django.core.paginator import Paginator

@login_required
def employee_list(request):
    employees = employeeModel.objects.filter(is_deleted=False).order_by('id')

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
        employee.is_deleted = True
        employee.deleted_at = timezone.now()
        employee.save()
        return redirect('employee_list')
    return render(request, 'employee/employee_confirm_delete.html', {'employee': employee})


@login_required
def employee_detail(request, id):
    employee = get_object_or_404(employeeModel, id=id)
    return render(request, 'employee/employee_detail.html', {
        'employee': employee
    })
