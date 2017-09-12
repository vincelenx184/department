from django import forms
from .models import EmployeeDetail
from crispy_forms.helper import FormHelper

class EmployeeDetailAddEmployeeForm(forms.ModelForm):

    helper = FormHelper()
    helper.form_show_labels = False


    class Meta:

        model = EmployeeDetail
        fields = ['first_name', 'last_name', 'email']

        def clean_email(self):
            email = self.clean_data.get('email')

            return email



