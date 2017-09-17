from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.template.loader import get_template

from .models import EmployeeDetail
from .forms import EmployeeDetailAddEmployeeForm


def names(request):

    details = EmployeeDetail.objects.all()

    template = 'staff/names.html'

    context = {

        'details': details,

    }

    return render(request, template, context)


def add_employee(request):

    form = EmployeeDetailAddEmployeeForm(request.POST or None)

    if form.is_valid():
        instance = form.save()


        if EmployeeDetail.objects.filter(email=instance.email).exists():
            messages.warning(request, 'This email already exists in the Database', 'alert alert-warning alert-dismissible')
            return redirect('staff:add_employee')

        else:
            instance.save()
            messages.success(request, 'This name has been submitted to the Database', 'alert alert-success alert-dismissible')
            return redirect('staff:add_employee')

    context = {

        'form': form,
  }



    template = 'staff/add_employee.html'

    return render(request, template, context)


def details(request, pk):

    named = get_object_or_404(EmployeeDetail, pk=pk)

    context = {

        'named': named,
    }

    template = 'staff/details.html'

    return render(request, template, context)


def edit_employee(request, pk):
    named = get_object_or_404(EmployeeDetail, pk=pk)

    if request.method == 'POST':
        form = EmployeeDetailAddEmployeeForm(request.POST, instance=named)

        if form.is_valid():
            named = form.save()

        return redirect('staff:details', pk=named.pk)


    else:
        form = EmployeeDetailAddEmployeeForm(instance=named)

    context = {

         'form': form,

    }

    template = 'staff/add_employee.html'

    return render(request, template, context)





