from django import forms
from Home.models import ChapterOneWeekOne,ChapterOneWeekTwo,ChapterTwoWeekOne,ChapterTwoWeekTwo,ChapterThreeWeekOne,ChapterThreeWeekTwo
Disciple_initiative = (
        ('Y', "Owns Initiative"),
        ('N', "Parent Initiative"))
    

class ChapterOneWeekOneForm(forms.ModelForm):     
    ChapterOneWeekOneQuestionOne = forms.ChoiceField(label="Choose to eat more healthy",help_text='Eat a fruit you like each day for one week',required=True, widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=Disciple_initiative)
    ChapterOneWeekOneQuestionTwo = forms.ChoiceField(label="Keep your body hidrated",help_text='Pay attention when you experience thurst. Keep a botle of fresh water around you', required=True, widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=Disciple_initiative)
    ChapterOneWeekOneQuestionThree = forms.ChoiceField(label="Skip fast-food/junk food",help_text='Junk food is making you tired and weak. Choose a healthier meal when you eat', required=True, widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=Disciple_initiative)
    
    class Meta():
        model = ChapterOneWeekOne
        fields = ["ChapterOneWeekOneQuestionOne", "ChapterOneWeekOneQuestionTwo","ChapterOneWeekOneQuestionThree"]

class ChapterOneWeekTwoFrom(forms.ModelForm):
    
    ChapterOneWeekTwoQuestionOne = forms.ChoiceField(label="Train for Jiu-Jitsu",help_text='Attend the classes two times a week', required=True, widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=Disciple_initiative)
    ChapterOneWeekTwoQuestionTwo = forms.ChoiceField(label="Take care your body hygiene",help_text='Shower, wash your hands and brush your teeth at least two times a day', required=True, widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=Disciple_initiative)
    ChapterOneWeekTwoQuestionThree = forms.ChoiceField(label="Keep your mind busy",help_text="Learn something new every day, perhaps a word you didnt know you didn't know yesturday.", required=True, widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=Disciple_initiative)
    
    class Meta():
        model = ChapterOneWeekTwo
        fields = ["ChapterOneWeekTwoQuestionOne","ChapterOneWeekTwoQuestionTwo","ChapterOneWeekTwoQuestionThree"]

class ChapterTwoWeekOneForm(forms.ModelForm):
    
    
    ChapterTwoWeekOneQuestionOne = forms.ChoiceField(label="Talk to people",help_text='Talk to your friends but also to other children you do not know so you can create a new conexion',required=True, widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=Disciple_initiative)
    ChapterTwoWeekOneQuestionTwo = forms.ChoiceField(label="Help people around you",help_text='If someone has a bad day,talk with them and listen to their problems',required=True, widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=Disciple_initiative)
    ChapterTwoWeekOneQuestionThree = forms.ChoiceField(label="Practice sharing",help_text='If someone needs your help or an item from you, share it with them.',required=True, widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=Disciple_initiative)
    
    class Meta():
        model = ChapterTwoWeekOne
        fields = ["ChapterTwoWeekOneQuestionOne","ChapterTwoWeekOneQuestionTwo", "ChapterTwoWeekOneQuestionThree"]

class ChapterTwoWeekTwoForm(forms.ModelForm):
    
    ChapterTwoWeekTwoQuestionOne = forms.ChoiceField(label="Keep a positive attitude",help_text='Choose to play outside with a friend over playing on phone or computer',required=True, widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=Disciple_initiative)
    ChapterTwoWeekTwoQuestionTwo = forms.ChoiceField(label="Be social and friendly",help_text='Invite your firends over to play and make homeworks together.',required=True, widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=Disciple_initiative)
    ChapterTwoWeekTwoQuestionThree = forms.ChoiceField(label="Talk to your parents",help_text='Choose to be friend with your parents. They are the greatest',required=True, widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=Disciple_initiative)
    
    class Meta():
        model = ChapterTwoWeekTwo
        fields = ["ChapterTwoWeekTwoQuestionOne","ChapterTwoWeekTwoQuestionTwo","ChapterTwoWeekTwoQuestionThree"]

class ChapterThreeWeekOneForm(forms.ModelForm): 
    
    ChapterThreeWeekOneQuestionOne = forms.ChoiceField(label="Help your parents",help_text='Offer your support to your parrent. Help them at the households tasks',required=True, widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=Disciple_initiative)
    ChapterThreeWeekOneQuestionTwo = forms.ChoiceField(label="Meet your deadline",help_text='Do your homework everyday or the task your parents assigned it to you',required=True, widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=Disciple_initiative)
    ChapterThreoWeekOneQuestionThree = forms.ChoiceField(label="Take care of your belongings",help_text='Value your stuff so they will last longer.You will be thankful to use them longer.',required=True, widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=Disciple_initiative)
    

    class Meta():
        model = ChapterThreeWeekOne
        fields = ["ChapterThreeWeekOneQuestionOne","ChapterThreeWeekOneQuestionTwo","ChapterThreoWeekOneQuestionThree"]

class ChapterThreeWeekTwoForm(forms.ModelForm):   
    
    ChapterThreeWeekTwoQuestionOne = forms.ChoiceField(label="Be honest",help_text='Always answer to your actions, even if they are bad',required=True, widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=Disciple_initiative)
    ChapterThreeWeekTwoQuestionTwo = forms.ChoiceField(label="Keep your promises",help_text='Keep your word and finish what you have started',required=True, widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=Disciple_initiative)
    ChapterThreeWeekTwoQuestionThree = forms.ChoiceField(label="Be thankful",help_text='Be happy with what you have. and learn for what you whish to have',required=True, widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=Disciple_initiative)
    
    class Meta():
        model = ChapterThreeWeekTwo
        fields = ["ChapterThreeWeekTwoQuestionOne","ChapterThreeWeekTwoQuestionTwo","ChapterThreeWeekTwoQuestionThree"]

