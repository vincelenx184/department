from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.template.loader import get_template

from .models import Employee
from .forms import EmployeeAddEmployeeForm


def list_of_employees(request):

    emps = Employee.objects.all()

    template = 'staff/list_of_employees.html'

    context = {
       'emps': emps,
    }

    return render(request, template, context)


