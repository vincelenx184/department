from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^names/', views.names, name='names'),

]