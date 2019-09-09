from django.shortcuts import render
from django.db.models import Max
from Home.forms import ContactForm, ChapterOneWeekOneForm,ChapterOneWeekTwoFrom,ChapterTwoWeekOneForm,ChapterTwoWeekTwoForm,ChapterThreeWeekOneForm,ChapterThreeWeekTwoForm
from UserManager.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from Home.models import InstructorProfile,ChapterOneWeekOne,ChapterOneWeekTwo,ChapterTwoWeekOne,ChapterTwoWeekTwo,ChapterThreeWeekOne,ChapterThreeWeekTwo
from UserManager.models import UserProfileInfo
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string

def send_us_email(request, ChapterOneProgress, ChapterTwoProgress,  ChapterThreeProgress):

    user = request.user.username
    mail_subject ="User {} has been making progress on his journey chapter data".format(user)
    message = render_to_string('Home/home_userdata.html', {
        'user': user,
        "ChapterOneProgress": ChapterOneProgress,
        "ChapterTwoProgress": ChapterTwoProgress,
        "ChapterThreeProgress": ChapterThreeProgress,
        })

    to_email = 'emanuel.ciobanu1921@gmail.com'
          
    send_mail(mail_subject, message, 'emanuel.ciobanu1921@gmail.com', [to_email], fail_silently=False)
            
def get_profile_photo(request):
    user = request.user.username
    user_main_data = User.objects.get(username=str(user))
    #print(user_main_data.id)
    user_second_data = UserProfileInfo.objects.get(user_id=user_main_data.id)
    #print(user_second_data)
    profile_pic = user_second_data.profile_pic
    return profile_pic

def home(request):
    if(request.user.is_authenticated):
        profile_pic = get_profile_photo(request)
        if(profile_pic):
            return render(request,'Home/home_live.html',{'profile_photo': profile_pic})
        else:
            return render(request,'Home/home_live.html')

def test_data(request, obj):
    id_user_instance = User.objects.get(id=request.user.id)
    try:
        check = obj.objects.get(user_id=id_user_instance.id)
    except obj.DoesNotExist:
        check = None

    return check, id_user_instance
 
def get_progressChOne(request):
    
        counterChOneWkOne = 0
        id_user_instance = User.objects.get(id=request.user.id)
        try:
            try:
                check = ChapterOneWeekOne.objects.all().filter(user_id=id_user_instance.id).values()
                vl = check[0].values()
                for x in vl:
                    if x=="Y":
                        counterChOneWkOne +=20
                    elif x=="N":
                        counterChOneWkOne +=10
                    else:
                        pass
            except:
                pass
        except ChapterOneWeekOne.DoesNotExist:
            pass

        
        counterChOneWkTwo = 0
        id_user_instance = User.objects.get(id=request.user.id)
        try:
            try:
                check = ChapterOneWeekTwo.objects.all().filter(user_id=id_user_instance.id).values()
                vl = check[0].values()
                for x in vl:
                    if x=="Y":
                        counterChOneWkTwo +=20
                    elif x=="N":
                        counterChOneWkTwo +=10
                    else:
                        pass
            except:
                pass

        except ChapterOneWeekTwo.DoesNotExist:
            pass
        
        ChapterOneSum = counterChOneWkOne + counterChOneWkTwo

        PrChapterOneSum = (ChapterOneSum * 100) / 120
        return int(PrChapterOneSum)

def get_progressChTwo(request):
    
        counterChOneWkOne = 0
        id_user_instance = User.objects.get(id=request.user.id)
        try:
            check = ChapterTwoWeekOne.objects.all().filter(user_id=id_user_instance.id).values()
            try:
                vl = check[0].values()
                for x in vl:
                    if x=="Y":
                        counterChOneWkOne +=20
                    elif x=="N":
                        counterChOneWkOne +=10
                    else:
                        pass
            except:
                pass
        except ChapterTwoWeekTwo.DoesNotExist:
            pass

        
        counterChOneWkTwo = 0
        id_user_instance = User.objects.get(id=request.user.id)
        try:
            check = ChapterTwoWeekTwo.objects.all().filter(user_id=id_user_instance.id).values()
            try:
                vl = check[0].values()
                for x in vl:
                    if x=="Y":
                        counterChOneWkTwo +=20
                    elif x=="N":
                        counterChOneWkTwo +=10
                    else:
                        pass
            except:
                pass
        except ChapterTwoWeekTwo.DoesNotExist:
            pass
        
        ChapterOneSum = counterChOneWkOne + counterChOneWkTwo

        PrChapterTwoSum = (ChapterOneSum * 100) / 120
        return int(PrChapterTwoSum)

def get_progressChThree(request):
    counterChOneWkOne = 0
    id_user_instance = User.objects.get(id=request.user.id)
    try:
        check = ChapterThreeWeekOne.objects.all().filter(user_id=id_user_instance.id).values()
        try:
            vl = check[0].values()
            for x in vl:
                if x=="Y":
                    counterChOneWkOne +=20
                elif x=="N":
                    counterChOneWkOne +=10
                else:
                    pass
        except:
            pass
    except ChapterThreeWeekTwo.DoesNotExist:
        pass

        
    counterChOneWkTwo = 0
    id_user_instance = User.objects.get(id=request.user.id)
    try:
        check = ChapterThreeWeekTwo.objects.all().filter(user_id=id_user_instance.id).values()
        try:
            vl = check[0].values()
            for x in vl:
                if x=="Y":
                    counterChOneWkTwo +=20
                elif x=="N":
                    counterChOneWkTwo +=10
                else:
                    pass
        except:
            pass
    except ChapterThreeWeekTwo.DoesNotExist:
        pass
        
    ChapterOneSum = counterChOneWkOne + counterChOneWkTwo

    PrChapterTwoSum = (ChapterOneSum * 100) / 120
    return int(PrChapterTwoSum)


def my_journey(request):
    if(request.user.is_authenticated):
        profile_pic = get_profile_photo(request)
        if request.method == 'POST':
            check, current_user = test_data(request, ChapterOneWeekOne)
            if check is None:    
                chapter_one_weekone = ChapterOneWeekOneForm(data=request.POST)
                if chapter_one_weekone.is_valid():
                    chapter_one_weekone = chapter_one_weekone.save(commit=False)
                    chapter_one_weekone.user =  current_user
                    chapter_one_weekone.save()
                    return redirect('/home/my_journey/')
                else:
                    print(chapter_one_weekone.errors)
            else:
                chapter_one_weekone = None

            check, current_user = test_data(request, ChapterOneWeekTwo)
            if check is None:    
                chapter_one_weektwo =ChapterOneWeekTwoFrom(data=request.POST)
                if chapter_one_weektwo.is_valid():
                    chapter_one_weektwo = chapter_one_weektwo.save(commit=False)
                    chapter_one_weektwo.user =  current_user
                    chapter_one_weektwo.save()
                    return redirect('/home/my_journey/')
                else:
                    print(chapter_one_weektwo.errors)
            else:
                chapter_one_weektwo = None  

            check, current_user = test_data(request, ChapterTwoWeekOne)   
            if check is None:    
                chapter_two_weekone = ChapterTwoWeekOneForm(data=request.POST)
                if chapter_two_weekone.is_valid():
                    chapter_two_weekone = chapter_two_weekone.save(commit=False)
                    chapter_two_weekone.user =  current_user
                    chapter_two_weekone.save()
                    return redirect('/home/my_journey/')
                else:
                    print(chapter_two_weekone.errors)
            else:
                chapter_two_weekone = None  

            check, current_user = test_data(request, ChapterTwoWeekTwo)
            if check is None:    
                chapter_two_weektwo = ChapterTwoWeekTwoForm(data=request.POST)
                if chapter_two_weektwo.is_valid():
                    chapter_two_weektwo = chapter_two_weektwo.save(commit=False)
                    chapter_two_weektwo.user =  current_user
                    chapter_two_weektwo.save()
                    return redirect('/home/my_journey/')
                else:
                    print(chapter_two_weektwo.errors)
            else:
                chapter_two_weektwo = None
            
            check, current_user = test_data(request, ChapterThreeWeekOne)
            if check is None:    
                chapter_three_weekone = ChapterThreeWeekOneForm(data=request.POST)
                if chapter_three_weekone.is_valid():
                    chapter_three_weekone = chapter_three_weekone.save(commit=False)
                    chapter_three_weekone.user =  current_user
                    chapter_three_weekone.save()
                    return redirect('/home/my_journey/')
                else:
                    print(chapter_three_weekone.errors)
            else:
                chapter_three_weekone = None


            check, current_user = test_data(request, ChapterThreeWeekTwo)
            if check is None:    
                chapter_three_weektwo = ChapterThreeWeekTwoForm(data=request.POST)
                if chapter_three_weektwo.is_valid():
                    chapter_three_weektwo = chapter_three_weektwo.save(commit=False)
                    chapter_three_weektwo.user =  current_user
                    chapter_three_weektwo.save()
                    return redirect('/home/my_journey/')
                else:
                    print(chapter_three_weektwo.errors)
            else:
                chapter_three_weektwo = None
        else:
            check, current_user = test_data(request, ChapterOneWeekOne)
            if check is None:    
                chapter_one_weekone = ChapterOneWeekOneForm()
            else:
                chapter_one_weekone = None
            
            check, current_user = test_data(request, ChapterOneWeekTwo)
            if check is None:    
                chapter_one_weektwo = ChapterOneWeekTwoFrom()
            else:
                chapter_one_weektwo = None
            
            check, current_user = test_data(request, ChapterTwoWeekOne)
            if check is None:    
                chapter_two_weekone = ChapterTwoWeekOneForm()
            else:
                chapter_two_weekone = None
            
            check, current_user = test_data(request, ChapterTwoWeekTwo)
            if check is None:    
                chapter_two_weektwo = ChapterTwoWeekTwoForm()
            else:
                chapter_two_weektwo = None
            
            check, current_user = test_data(request, ChapterThreeWeekOne)
            if check is None:    
                chapter_three_weekone = ChapterThreeWeekOneForm()
            else:
                chapter_three_weekone = None
            
            check, current_user = test_data(request, ChapterThreeWeekTwo)
            if check is None:    
                chapter_three_weektwo = ChapterThreeWeekTwoForm()
            else:
                chapter_three_weektwo = None

            # Get user progress data for each Chapter
            ChapterOneProgress = get_progressChOne(request)
            ChapterTwoProgress = get_progressChTwo(request)
            ChapterThreeProgress =get_progressChThree(request)

            # Send user performance data
            send_us_email(request, ChapterOneProgress, ChapterTwoProgress,  ChapterThreeProgress)

        if(profile_pic):
            context = {
            "chapter_one_weekone": chapter_one_weekone,
            "chapter_one_weektwo": chapter_one_weektwo,
            "chapter_two_weekone": chapter_two_weekone,
            "chapter_two_weektwo": chapter_two_weektwo,
            "chapter_three_weekone": chapter_three_weekone,
            "chapter_three_weektwo": chapter_three_weektwo,
            "ChapterOneProgress": ChapterOneProgress,
            "ChapterTwoProgress": ChapterTwoProgress,
            "ChapterThreeProgress": ChapterThreeProgress,
            "profile_photo": profile_pic
            }
            return render(request,'Home/home_journey.html',context)
        else:
            context = {
            "chapter_one_weekone": chapter_one_weekone,
            "chapter_one_weektwo": chapter_one_weektwo,
            "chapter_two_weekone": chapter_two_weekone,
            "chapter_two_weektwo": chapter_two_weektwo,
            "chapter_three_weekone": chapter_three_weekone,
            "chapter_three_weektwo": chapter_three_weektwo,
            "ChapterOneProgress": ChapterOneProgress,
            "ChapterTwoProgress": ChapterTwoProgress,
            "ChapterThreeProgress": ChapterThreeProgress,
            }
            return render(request,'Home/home_journey.html',context)

    else:
        return HttpResponse('You are not loged in. Please first log in to access this web page!')


def team(request):
    if(request.user.is_authenticated):
        instructors = InstructorProfile.objects.all()
        profile_data = UserProfileInfo.objects.all().select_related("user").all
        profile_pic = get_profile_photo(request)

        if(profile_pic):
            context = {
                "all_instructors": instructors,
                "all_profiles" : profile_data,
                "profile_photo" : profile_pic   
            }
            return render(request,'Home/home_team.html',context)
        else:
            context = {
                "all_instructors": instructors,
                "all_profiles" : profile_data,
            }
            return render(request,'Home/home_team.html', context)


def contact(request):
      if(request.user.is_authenticated):
        profile_pic = get_profile_photo(request)
        if request.method == 'POST':
            my_contactform = ContactForm(data=request.POST)
            if my_contactform.is_valid():
                print(my_contactform)
                
            else:
                print(my_contactform.errors)
        else:
           my_contactform = ContactForm() 
            
        if(profile_pic):
            return render(request,'Home/home_contact.html',
                {
                    'profile_photo': profile_pic,
                    'contact_form' : my_contactform
                })
        else:
            return render(request,'Home/home_contact.html', {'contact_form' : my_contactform})

    
