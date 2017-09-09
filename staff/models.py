from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

class EmployeeDetail(models.Model):
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    id_number = models.IntegerField()
    currently_employed = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.last_name)
        super(EmployeeDetail, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('staff:EmployeeDetail', args=[self.slug])

    def __str__(self):
        return self.last_name

    



