from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Coach(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
        )

    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    email = models.EmailField()
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    skype = models.CharField(max_length=30)
    description = models.TextField()


    def __unicode__(self):
        return self.user.first_name 