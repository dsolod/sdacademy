from django.db import models
from coaches.models import Coach

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=30)
    short_description = models.CharField(max_length=60)
    description = models.TextField()
    coach = models.ForeignKey(Coach, null=True, related_name='coach_courses')
    assistant = models.ForeignKey(Coach, null=True, related_name='assistant_courses')

    def __unicode__(self):
        return self.name
#name, short_description, description, coach

class Lesson(models.Model):
    subject = models.CharField(max_length=30)

    description = models.TextField()
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()

    def __unicode__(self):
        return self.subject

