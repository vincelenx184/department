from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

from .models import EmployeeDetail
from .forms import EmployeeDetailAddEmployeeForm


def names(request):


    details = EmployeeDetail.objects.all()

    template = 'staff/names.html'

    context = {

        'details': details

    }

    return render(request, template, context)


def add_employee(request):

    form = EmployeeDetailAddEmployeeForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)

        if EmployeeDetail.objects.filter(email=instance.email).exists():
            messages.warning(request, 'This email already exists in the Database', 'alert alert-warning alert-dismissible')
            return redirect('staff:add_employee')

        else:
            instance.save()
            messages.success(request, 'This name has been submitted to the Database', 'alert alert-success alert-dismissible')
            return redirect('staff:add_employee')

    context = {

        'form': form
  }



    template = 'staff/add_employee.html'

    return render(request, template, context)


def update_employee(request):

    update = EmployeeDetail.





