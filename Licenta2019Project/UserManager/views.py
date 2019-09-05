from django.shortcuts import render
from UserManager.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from .token import account_activation_token
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.models import User
from django.shortcuts import redirect


def index(request):
    if(request.user.is_authenticated):
        return redirect('/home/')
    else:
        return render(request,'UserManager/index.html')


@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    # Boolean value to know if an user is registered
    registered = False

    # If user data is submited
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)                 # Instantiate the UserForm Form class
        profile_form = UserProfileInfoForm(data=request.POST)   # Instantiate the UserProfileInfoForm class
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)                             # Saves the user authentification data into the SQLite database
            user.is_active = False     
            print(user.password)                                # Deactivates the user until the e-mail confirmation
            #user.set_password(user.password)                    # Set password data column with the submited user password
            user.save()                                         
            current_site = get_current_site(request)
    
            # Email activation sing-in actions
            token = account_activation_token.make_token(user)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('UserManager/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':token,
            })
            to_email = user_form.cleaned_data.get('email')
          
            send_mail(mail_subject, message, 'emanuel.ciobanu1921@gmail.com', [to_email], fail_silently=False)
            
            
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'UserManager/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.is_superuser =True
        user.is_staff = True
        user.save()
        login(request, user)
        # return redirect('home')
        response = redirect('/home/')
        return response
        #return render(request,'UserManager/thank_you_for_authentifaction.html')

    else:
        return HttpResponse('Activation link is invalid!')


"""def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.is_active = False  # Not sure
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'UserManager/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
"""
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            print("Bine pana aici!")
            if user.is_active:
                login(request,user)
                print("Someone tried to login and succeded!.")
                print("They used username: {} and password: {}".format(username,password))
                response = redirect('/home/')
                return response
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'UserManager/login.html', {})

# Create your views here.
