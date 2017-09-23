from django.contrib import admin

from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'last_name', 'first_name', 'created_profile', 'currently_employed')
    list_filter = ('currently_employed', 'created_profile', 'updated_profile', 'coordinator')
    search_fields = ('job_title', 'job_description')
    prepopulated_fields = {'slug': ('job_title', )}


admin.site.register(Employee, EmployeeAdmin)


