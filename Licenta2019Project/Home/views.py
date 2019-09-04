from django.shortcuts import render
from UserManager.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User

def home(request):
    return render(request,'Home/home_live.html')

