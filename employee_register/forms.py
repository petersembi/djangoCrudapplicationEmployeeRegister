from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'
        # fields = ('fullname','emp_code','mobile,'position')

        labels = {
            'fullname': 'Full Name',
            'emp_code': 'Employee Code'
        }
    