from django.shortcuts import render, get_object_or_404
from django.contrib import messages

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

        if EmployeeDetail.objects.filter(id=instance.id).exists():
            messages.warning(request, 'You already exist in the data-base', 'alert alert-warning alert-dismissible')

        else:
            instance.save()
            messages.success(request, 'Your name has been submitted', 'alert alert-success alert-dismissible')

    context = {

        'form': form

    }



    template = 'staff/add_employee.html'

    return render(request, template, context)







