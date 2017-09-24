from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^employees/list/$', views.list_of_employees, name='list_of_employees'),
    url(r'^employees/add-employee/$', views.add_employee, name='add_employee'),
    url(r'^employees/(?P<slug>[-\w]+)/edit-employee/$', views.edit_employee, name='edit_employee'),
    url(r'^employees/(?P<slug>[-\w]+)/delete-employee/$', views.delete_employee, name='delete_employee'),
    url(r'^employees/employee-detail/$', views.employee_detail, name='employee_detail'),
]


