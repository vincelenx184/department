from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^names/', views.names, name='names'),
    url(r'^add_employee/', views.add_employee, name='add_employee'),

]


