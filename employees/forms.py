# employees/forms.py
from django import forms
from .models import employeeModel

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = employeeModel
        exclude = ['is_deleted', 'deleted_at']

