from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^employees/list/$', views.list_of_employees, name='list_of_employees'),
    url(r'^employees/list/add_employee/$', views.add_employee, name='add_employee'),
    url(r'^employees/(?P<slug>[-\w]+)/edit_employee/$', views.edit_employee, name='edit_employee'),
    url(r'^employees/(?P<slug>[-\w]+)/delete_employee/$', views.delete_employee, name='delete_employee'),
]


