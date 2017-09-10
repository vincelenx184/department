from django.shortcuts import render, get_object_or_404
from .models import EmployeeDetail


def names(request):

    template = 'staff/names.html'

    details = EmployeeDetail.objects.all()

    context = {

        'details': details

    }

    return render(request, template, context)





