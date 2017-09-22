from django.db import models


class EmployeeDetail(models.Model):

    EMPLOYEE_STATUS = (

        ('Active Employee', 'Active Employee'),
        ('Deactivated Employee', 'Deactivated Employee')

    )

    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    phone_number = models.IntegerField(blank=True,null=True)
    id_number = models.IntegerField(blank=True, null=True)
    currently_employed = models.CharField(max_length=30, choices=EMPLOYEE_STATUS, default=False)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.last_name







    



