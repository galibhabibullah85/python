from django import forms as f
from django.forms import Form as F
from django.contrib.auth.models import User



class login(F):
  usr_mail = f.EmailField(label="Email address", max_length=30, initial="abc@me.in")
  
  usr_pwd = f.CharField(label="Password",min_length=8, initial="12345678", widget=f.TextInput(attrs={ "type":"password", }))
  




"""
class signup(F):
  usr_name = f.CharField(label="Your name", max_length=20, initial="Jordi")
  
  usr_mail = f.EmailField(label="Email address", max_length=30, initial="abc@me.in")
  
  usr_pwd = f.CharField(label="Password",min_length=8, initial="12345678", widget=f.TextInput(attrs={ "type":"password", }))
  
  #usr_sex = f.CharField(label="Male", widget=f.TextInput(attrs={ "type":"radio", "value":"male", "name":"sex", }))
  #usr_sex = f.CharField(label="Female", widget=f.TextInput(attrs={ "type":"radio","value":"female", "name":"sex", }))
""" 
  
  
  
"""
#for creating form according to model
import models

class form_name(models.ModelForm):
  class Meta:
    model = `the model that we want to convert into form`
    fields = "__all__"#for all fields
    fields = ('field_name',...)#for specific fields
"""



class UserModelForm(f.ModelForm):
  password = f.CharField(widget=f.PasswordInput())#over-writting the user.password field
  class Meta():
    model = User
    fields = ('username','email','password')