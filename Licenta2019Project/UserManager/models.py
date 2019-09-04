from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


"""class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=0) # Set the age of the user
    height = models.IntegerField(default=0) # Set the height of the user
    kilograms = models.FloatField(null=True, default=0)

    def __str__(self):
        return self.user.username

"""
class UserProfileInfo(models.Model):
    Flash = 'Fl'
    Hulk = 'Hl'
    Batman = 'Bt'
    Superman = 'Sp'
    
    
    SuperPowerChoice = [
        (Flash, 'Flah the gratest'),
        (Hulk, 'Hulk all mighty'),
        (Batman, 'Batman, the strategic'),
        (Superman, 'Superman the call to advanture'),
    ]

    age = models.FloatField(null=True,
        validators =[MinValueValidator(5.0),
                     MaxValueValidator(100.0)
        ] 
    )
    kg = models.FloatField(null=True,
        validators =[MinValueValidator(5.0),
                     MaxValueValidator(100.0)
        ]
    )
    height = models.FloatField(null=True,
        validators =[MinValueValidator(5.0),
                     MaxValueValidator(100.0)
        ]
    )
    super_power = models.CharField(
        max_length=2,
        choices=SuperPowerChoice,
        default=Flash,
    )
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    #user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User', null=True)
    def __str__(self):
        return self.user.username