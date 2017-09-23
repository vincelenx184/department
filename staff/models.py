from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from django.contrib.auth.models import User

class Employee(models.Model):
    EMPLOYEE_STATUS = (

        ('Active Employee', 'Active Employee'),
        ('Deactivated Employee', 'Deactivated Employee'),

    )

    coordinator = models.ForeignKey(User, related_name='name_creator')
    job_title = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    id_number = models.IntegerField(default=0)
    currently_employed = models.CharField(max_length=30, choices=EMPLOYEE_STATUS)
    email = models.EmailField()
    slug = models.SlugField(max_length=250, unique=True)
    created_profile = models.DateTimeField(auto_now_add=True)
    updated_profile = models.DateTimeField(auto_now=True)
    job_description = models.TextField()


    def save(self, *args, **kwargs):
        self.slug = slugify(self.job_title)
        super(Employee, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('staff:employee_detail', args=[self.slug])

    def __str__(self):
        return self.job_title












    



