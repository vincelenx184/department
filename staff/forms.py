from django import forms
from .models import EmployeeDetail


class EmployeeDetailAddEmployeeForm(forms.ModelForm):



    class Meta:

        model = EmployeeDetail
        fields = ['first_name', 'last_name', 'phone_number']



