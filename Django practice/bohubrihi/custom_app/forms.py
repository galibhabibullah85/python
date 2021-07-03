#customly created file
#same structure as model.py
from django import forms as f
from django.forms import Form as F

class first_form(F):
  date = f.DateField(label="My date",widget=f.TextInput( attrs={ "type":" date", } ))
  
  usr_name = f.CharField(required=False,initial="hi")
  #<input name='usr_name' type='text'>
  #required is by-default always True
  #initial argument is equivalent to value html attribute
  
  usr_email = f.EmailField(label="Your email", widget=f.TextInput( attrs={ 'placeholder':"Your email",
    'style':"border:2px solid black",  } ) )
  #<input name='usr_email' type='email'>
  #label argument is equivalent to label html tag
  
#python automitically sets required attribute to all the input tags

#for all the arguments available in form's __Field() visit "https://docs.djangoproject.com/en/3.2/ref/forms/fields/"