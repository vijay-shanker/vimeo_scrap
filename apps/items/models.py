from django.db import models

# Create your models here.
class Item(models.Model):
    username = models.CharField(max_length=100)
    userprofile = models.CharField(max_length=100)
    is_paying_user = models.BooleanField(default=False)
    has_video = models.BooleanField(default=True)
    is_staff_pick = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.username
    
    
    
