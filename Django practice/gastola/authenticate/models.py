from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User

# Create your models here.
class UserInfo(Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  
  phone = models.CharField(max_length=17,blank=False,unique=True)
  home_address = models.CharField(max_length=100,blank=False)
  facebook_id = models.URLField(max_length=100,blank=False,unique=True)
  
  def __str__(self):
    return self.user.username