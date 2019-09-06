from Home.models import  InstructorProfile
from django.core.files import File

trainer_one = InstructorProfile(first_name="Liviu", second_name="Surlas", rank_title="black belt", description="Head coach and creator of TitansKidsEvolutionSystem")
trainer_one.save()
trainer_two = InstructorProfile(first_name="Sergiu", second_name="Scrob", rank_title="blue belt", description="Coach - age group - 7")
trainer_two.save()
trainer_three = InstructorProfile(first_name="Daniel", second_name="Craciun", rank_title="purpule belt", description="Coach - age group - 7+")
trainer_three.save()
trainer_four = InstructorProfile(first_name="Emanuel", second_name="Ciobanu", rank_title="blue belt", description="Coach - age group - 7")
trainer_four.save()

trainer_one.profile_pic.save('liviu.jpg', File(open('media/trainer_pics/liviu.jpg', 'rb')))
trainer_two.profile_pic.save('sergiu.jpg', File(open('media/trainer_pics/sergiu.jpg', 'rb')))
trainer_three.profile_pic.save('daniel.jpg', File(open('media/trainer_pics/dani.jpg', 'rb')))
trainer_four.profile_pic.save('ema.jpg', File(open('media/trainer_pics/Ema.jpg', 'rb')))
