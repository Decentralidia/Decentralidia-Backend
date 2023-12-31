from django.db import models

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other/Non-Binary'),
    ('N', 'Prefer not to say')
)

class User(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=200)
    votes = models.CharField(max_length=300, default="", blank=True)
    age = models.IntegerField(default=0)  # Age in numbers and non-optional
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default="")
    likes_dislikes = models.CharField(max_length=100000, default="", blank=True)  # format: tweet_id:like/dislike#

    # # Efficiently get or create a user
    # user, created = UserModel.objects.get_or_create(fullname=fullname)
    
    # #If user is found but not created, update age and gender
    # if not created:
    # user.age = age
    # user.gender = gender
    # user.save()