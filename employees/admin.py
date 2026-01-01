from django.contrib import admin
from .models import employeeModel

@admin.register(employeeModel)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department', 'created_at')
    search_fields = ('name', 'email', 'department')


# Register your models here.
