from django.db import models
from courses.models import Course

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    email = models.EmailField()

    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    skype = models.CharField(max_length=30)
    courses = models.ManyToManyField(Course)


    def __unicode__(self):
        return self.name + ' ' + self.surname

    def fullname(self):
        return self.name + ' ' + self.surname

