from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

class EmployeeDetail(models.Model):
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    id_number = models.IntegerField(blank=True, null=True)
    currently_employed = models.BooleanField(default=False)


    def __str__(self):
        return self.last_name

    



