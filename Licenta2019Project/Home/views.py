from django.shortcuts import render
from UserManager.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from UserManager.models import UserProfileInfo

def get_profile_photo(request):
    user = request.user.username
    user_main_data = User.objects.get(username=str(user))
    #print(user_main_data.id)
    #user_second_data = UserProfileInfo.objects.get(user_id=user_main_data.id)
    #print(user_second_data)
    #profile_pic = user_second_data.profile_pic
    profile_pic=''
    return profile_pic

def home(request):
    if(request.user.is_authenticated):
        profile_pic = get_profile_photo(request)
        if(profile_pic):
            return render(request,'Home/home_live.html',{'profile_photo': profile_pic})
        else:
            return render(request,'Home/home_live.html')
def team(request):
    if(request.user.is_authenticated):
        profile_pic = get_profile_photo(request)
        if(profile_pic):
            return render(request,'Home/home_team.html',{'profile_photo': profile_pic})
        else:
            return render(request,'Home/home_team.html')