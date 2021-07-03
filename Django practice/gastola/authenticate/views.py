from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from authenticate.models import UserInfo
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
#from authenticate.forms import *

# Create your views here.
def log_in(request):
  diction = {
    'title': "GASTOLA | Log-",
    'errors':[]
  }
  
  if request.method=="POST":
    try:
      form_data = request.POST
      
      usrname = form_data.get('email').split('@')[0]
      pwd = form_data.get('password')
    except Exception as e:
      print(e)
      diction['errors'].append(e)
    else:
      usr = authenticate(username=usrname,password=pwd)
      if usr:
        if usr.is_active:
          login(request,usr)
          return redirect('/')
      else:
        diction['errors'].append('Mail or password did not matched!')
      
  return render(request,'auth/login.html',diction)
  
  
  
def signup(request):
  #usr_form = UserForm()
  #usr_info_form = UserInfoForm()
  diction = {
    'errors':[],
    'title':"GASTOLA | Sign-up",
    #'usr_form':usr_form,
    #'usr_info_form':usr_info_form,
  }
  
  if request.method=="POST":
    form_data = request.POST
    
    try:
      fname = form_data.get('first_name')
      lname = form_data.get('last_name')
      mail = form_data.get('email')
      pwd = form_data.get('password')
      phn = form_data.get('phone')
      addr = form_data.get('home_address')
      fb = form_data.get('facebook_id')
    except Exception as e:
      print(e)
      diction['errors'].append(e)
      
      return render(request,'auth/signup.html',diction)
    else:
      if len(User.objects.filter(email=mail))!=0 or len(UserInfo.objects.filter(phone=phn))!=0 or len(UserInfo.objects.filter(facebook_id=fb))!=0:
        diction['errors'].append('Mail or phone-number or facebook-id already exists!')
        return render(request,'auth/signup.html',diction)
      
      dj_db = User()
      dj_db.first_name = fname
      dj_db.last_name = lname
      dj_db.email = mail
      dj_db.username = mail.split('@')[0]
      dj_db.password = pwd
      dj_db.set_password(dj_db.password)
      dj_db.save()
      
      db = UserInfo()
      db.user = dj_db
      db.phone = phn
      db.home_address = addr
      db.facebook_id = fb
      db.save()
      
      return redirect(reverse('auth:login'))

  return render(request,'auth/signup.html',diction)
  
  
@login_required
def log_out(request):
  logout(request)
  return redirect('/')