from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

# from http.client import HTTPResponse
# from django.shortcuts import get_object_or_404, render
# from django.template import loader
# from django.http import HttpResponse, HttpResponseRedirect
# from django.urls import reverse
# Create your views here.

def employee_list(request):
    context  = {'employee_list' : Employee.objects.all()}
    return render(request, "employee_register/employee_list.html",context)

def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
            
        return render(request, "employee_register/employee_form.html", {'form':form})
    else:
        if id == 0:         
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance = employee)
        # check whether the form is valid
        if form.is_valid():
            form.save()
        return redirect('/employee/list')

def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')


