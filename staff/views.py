from django.shortcuts import render, get_object_or_404
from .models import EmployeeDetail


def names(request):



    details = EmployeeDetail.objects.all()

    template = 'staff/names.html'

    context = {

        'details': details

    }

    return render(request, template, context)





