"""
To run the script use the command:

python manage.py runscript clean_data.py

Runscript uses the pip package - dajango-extensions=2.2.1

"""

from UserManager.models import  UserProfileInfo
from Home.models import  InstructorProfile
from django.contrib.auth.models import User

UserProfileInfo.objects.all().delete()
User.objects.all().delete()
InstructorProfile.objects.all().delete()


