from django.db import models
from django.utils import timezone

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=60)
    message = models.CharField(max_length=600)
    from_email = models.EmailField(max_length=60)
    create_date = models.DateTimeField(editable=False) 

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
        	self.create_date = timezone.now()
        return super(Feedback, self).save(*args, **kwargs)
