from django.shortcuts import render
from staff.models import EmployeeDetail

def home(request):

    template = 'home.html'


    return render(request, template)


