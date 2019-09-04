from django.conf.urls import url
from . import views


# SET THE NAMESPACE!
app_name = 'Home'


# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^$',  views.home, name='home'),
]