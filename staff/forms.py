from django import forms
from .models import Employee
from crispy_forms.helper import FormHelper


class EmployeeAddEmployeeForm(forms.ModelForm):

    helper = FormHelper()
    helper.form_show_labels = False

    class Meta:
        model = Employee

        widgets = {

            'job_title': forms.TextInput(attrs={'placeholder': 'Job Title'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'id_number': forms.TextInput(attrs={'placeholder': 'I.D. Number'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'currently_employed': forms.TextInput(attrs={'placeholder': 'Currently Employed'}),
        }

        fields = ('job_title', 'first_name', 'last_name', 'id_number', 'email', 'currently_employed')

        def clean_email(self):
            email = self.clean_data.get('email')
            return email



