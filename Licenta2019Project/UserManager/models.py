from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class UserProfileInfo(models.Model):
    Flash = 'Flash, the fastest'
    Hulk = 'Hulk, the strongest'
    CaptainAmerica = 'Captain, the strategic'
    Spiderman = 'Spiderman, the stickiest'
 
    SuperPowerChoice = [
        (Flash, 'Flash, the fastest'),
        (Hulk, 'Hulk, the strongest'),
        (CaptainAmerica, 'Captain, the strategic'),
        (Spiderman, 'Spiderman, the stickiest'),
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
        max_length=30,
        choices=SuperPowerChoice,
        default=Flash,
    )
    profile_pic = models.ImageField(upload_to='profile_pics',blank=False)
    #user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='use_extra', null=True)
    def __str__(self):
        return self.user.username
