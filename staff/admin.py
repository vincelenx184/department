from django.contrib import admin

from .models import EmployeeDetail

class EmployeeDetailAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('last_name', 'first_name',)

admin.site.register(EmployeeDetail, EmployeeDetailAdmin)

