from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^names/$', views.names, name='names'),
    url(r'^add_employee/$', views.add_employee, name='add_employee'),
    url(r'^details/(?P<pk>\d+)/$', views.details, name='details'),
    url(r'^edit_employee/(?P<pk>\d+)/$', views.edit_employee, name='edit_employee'),

]


