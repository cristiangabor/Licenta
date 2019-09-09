from django.db import models
from django.contrib.auth.models import User
from django import forms

class InstructorProfile(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    rank_title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.first_name

class ChapterOneWeekOne(models.Model):

    ChapterOneWeekOneQuestionOne = models.CharField(max_length=20, null=True)
    ChapterOneWeekOneQuestionTwo = models.CharField(max_length=20, null=True)
    ChapterOneWeekOneQuestionThree = models.CharField(max_length=20, null=True)
 
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='progress_ChOneWeekOne', null=True,unique=True)

    def __str__(self):
        return self.ChapterOneWeekOneQuestionOne
class ChapterOneWeekTwo(models.Model):

    ChapterOneWeekTwoQuestionOne = models.CharField(max_length=20, null=True)
    ChapterOneWeekTwoQuestionTwo = models.CharField(max_length=20, null=True)
    ChapterOneWeekTwoQuestionThree = models.CharField(max_length=20, null=True)
    

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='progress_ChOneWeekTwo', null=True,unique=True)

    def __str__(self):
        return self.ChapterOneWeekOneQuestionOne,self.ChapterOneWeekTwoQuestionTwo,self.ChapterOneWeekTwoQuestionThree


class ChapterTwoWeekOne(models.Model):

    ChapterTwoWeekOneQuestionOne = models.CharField(max_length=20, null=True)
    ChapterTwoWeekOneQuestionTwo = models.CharField(max_length=20, null=True)
    ChapterTwoWeekOneQuestionThree = models.CharField(max_length=20, null=True)
    
        
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='progress_ChTwoWeekOne', null=True)

    def __str__(self):
        return self.ChapterTwoWeekOneQuestionOne, self.ChapterTwoWeekOneQuestionTwo,self.ChapterTwoWeekOneQuestionThree

class ChapterTwoWeekTwo(models.Model): 

    ChapterTwoWeekTwoQuestionOne = models.CharField(max_length=20, null=True)
    ChapterTwoWeekTwoQuestionTwo = models.CharField(max_length=20, null=True)
    ChapterTwoWeekTwoQuestionThree = models.CharField(max_length=20, null=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='progress_ChTwoWeekTwo', null=True)

    def __str__(self):
        return self.ChapterTwoWeekTwoQuestionOne, self.ChapterTwoWeekTwoQuestionTwo, self.ChapterTwoWeekTwoQuestionThree


class ChapterThreeWeekOne(models.Model):
    ChapterThreeWeekOneQuestionOne = models.CharField(max_length=20, null=True)
    ChapterThreeWeekOneQuestionTwo = models.CharField(max_length=20, null=True)
    ChapterThreoWeekOneQuestionThree = models.CharField(max_length=20, null=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='progress_ChThreeWeekOne', null=True)

    def __str__(self):
        return self.ChapterThreeWeekOneQuestionOne, self.ChapterThreeWeekOneQuestionTwo, self.ChapterThreoWeekOneQuestionThree
    
class ChapterThreeWeekTwo(models.Model):    

    ChapterThreeWeekTwoQuestionOne = models.CharField(max_length=20, null=True)
    ChapterThreeWeekTwoQuestionTwo = models.CharField(max_length=20, null=True)
    ChapterThreeWeekTwoQuestionThree = models.CharField(max_length=20, null=True)
 
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='progress_ChThreWeekTwo', null=True)

    def __str__(self):
        return self.ChapterThreeWeekTwoQuestionOne, self.ChapterThreeWeekTwoQuestionTwo, self.ChapterThreeWeekTwoQuestionThree
