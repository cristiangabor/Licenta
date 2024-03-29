from django.conf.urls import url
from . import views


# SET THE NAMESPACE!
app_name = 'Home'


# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^$',  views.home, name='home'),
    url(r'^team/$', views.team, name='team'),
    url(r'^my_journey/$', views.my_journey, name='my_journey'),
    url(r'^contact/$', views.contact, name='contact'),
]