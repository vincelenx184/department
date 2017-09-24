from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.template.loader import get_template

from .models import Employee
from .forms import EmployeeAddEmployeeForm


def list_of_employees(request):

    employee = Employee.objects.all()

    template = 'staff/list_of_employees.html'

    context = {
       'employee': employee,
    }

    return render(request, template, context)


def add_employee(request):
    if request.method == "POST":
        form = EmployeeAddEmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.coordinator = request.user

            if Employee.objects.filter(email=employee.email).exists():
                messages.warning(request, 'This email already exists in our database!', 'alert alert-warning alert-dismissible')

            else:
                employee.save()
                messages.success(request, 'Employee has been added!')
                return redirect('staff:list_of_employees')
    else:
        form = EmployeeAddEmployeeForm()

    template = 'staff/add_employee.html'

    context = {'form': form, }

    return render(request, template, context)


def edit_employee(request, slug):

    employee = get_object_or_404(Employee, slug=slug)

    if request.method == 'POST':
        form = EmployeeAddEmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.coordinator = request.user
            employee.save()
            messages.success(request, 'Your Employee Profile has been updated!')
            return redirect('staff:list_of_employees')

    else:
        form = EmployeeAddEmployeeForm(instance=employee)

    template = 'staff/add_employee.html'

    context = {'form': form}

    return render(request, template, context)


def delete_employee(request, slug):

    employee = get_object_or_404(Employee, slug=slug)

    employee.delete()

    messages.success(request, "Employee has been deleted")

    return redirect('staff:list_of_employees')
















