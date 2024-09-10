from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
    
#Customer profile
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone= models.CharField(max_length=15,blank=True)
    address= models.CharField(max_length=200, blank=True)
    date_modified= models.DateTimeField(User,auto_now=True)
    old_cart= models.CharField(max_length=200,null=True, blank=True)

    def __str__(self):
        return self.user.username


#create a user profile by default when user register
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

#Automate the profile
post_save.connect(create_profile, sender=User)
        