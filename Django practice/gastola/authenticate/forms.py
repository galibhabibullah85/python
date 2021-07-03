from django import forms
from django.forms import ModelForm
from authenticate.models import UserInfo
from django.contrib.auth.models import User

class UserForm(ModelForm):
  password = forms.CharField(widget=forms.PasswordInput())
  class Meta:
    model = User
    fields = ('first_name','last_name','email','password')
    
    
class UserInfoForm(ModelForm):
  class Meta:
    model = UserInfo
    fields = ('phone','home_address','facebook_id')