from django.db import models as m
from django.db.models import Model as M
from django.contrib.auth.models import User


# Create your models here.
"""
class User(M):
  id = m.AutoField(primary_key=True)
  name = m.CharField( max_length=20, blank=False )
  mail = m.EmailField( max_length=30, blank=False )
  pwd = m.CharField( max_length=32, blank=False )
  
  def __str__(self):
    return self.name
"""

class UsrInfo(M):
  user_instance = m.OneToOneField(User,on_delete=m.CASCADE)
  
  def __str__(self):
    return self.user.username