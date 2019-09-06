from django.db import models

class InstructorProfile(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    rank_title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.first_name

