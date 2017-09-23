from django import forms
from .models import Employee


class EmployeeAddEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('job_title', 'first_name', 'last_name', 'id_number', 'email', 'currently_employed')

        def clean_email(self):
            email = self.clean_data.get('email')
            return email



