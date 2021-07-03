from django.shortcuts import render
from django.http import HttpResponse as hr
from authenticate.forms import login,UserModelForm
from authenticate.models import User

"""
Both redirects to another url:
from django.http import HttpResponseRedirect
from django.shortcuts import redirec
"""

"""
For declaring urls like {% url 'app_name:name' %} this in python file:
from django.urls import reverse
reverse('app_name:name')
"""
#HttpResponseRedirect(reverse('app_name:name'))
#redirect(reverse('app_name:name'))


# Create your views here.
def index(request):
  """
  For showing all the values inside a form:
  #all=User.objects.all()
  #login_form = login(instance=all)
  """
  login_form = login()
  context = {
    "login_form":login_form,
  }
  
  if request.method == "POST":
    usr_mail = request.POST.get("usr_mail")
    usr_pwd = request.POST.get("usr_pwd")
    
    try:
      #usr_db_mail = User.objects.all()#select * from 'table_name'
      
      usr_db_mail = User.objects.get(mail=usr_mail, pwd=usr_pwd )#this is for a single record #select * from 'table_name' where 'mail'=usr_mail and 'pwd'=usr_pwd
      
      #usr_db_mail = User.objects.filter(mail=usr_mail, pwd=usr_pwd )#this is for multiple records #select * from 'table_name' where 'mail'=usr_mail and 'pwd'=usr_pwd
      
    #usr_db_mail = User.objects.order_by("col_name", 'col_name2')#select * from 'table_name' order by 'col_name','col_name2'
    
    #many_query = User.objects.all().order_by('col_name', 'col_name2')
    except Exception:
      print(Exception("hellowjwjehdhrh"))
      
    """
    if usr_db.objects.value("mail")==usr_mail and usr_db.objects.value("pwd")==usr_pwd:
      return render(request, "store/index.html")
    """
  return render(request, "auth/login.html",context)





  
def sign_up(request):
#def sign_up(request,get_veriable_name):
  #sign_form = signup()
  sign_form = UserModelForm()
  if request.method == "POST":
    sign_form = UserModelForm(data=request.POST)
    
    if sign_form.is_valid():
      signup_info = sign_form.save()#commit=False does not saves the datas directly to database rather it is saving the datas into the variable
      signup_info.set_password(signup_info.password)#encripting the password
      signup_info.save()
    
    
    """
    usr_name = request.POST.get("usr_name")
    usr_mail = request.POST.get("usr_mail")
    usr_pwd = request.POST.get("usr_pwd")
    
    user_db = User()
    user_db.name = usr_name
    user_db.mail = usr_mail
    user_db.pwd = usr_pwd
    user_db.save()
      
    return index(request)
    """
    """
    -----------------------------------
    #for submitting form to model using ModelForm
    form = forms.ModelFormName()
    
    if request.method == "":
      form = forms.ModelFormName(request.POST)
      
      if form.is_valid():
        form.save(commit=True)
    -----------------------------------
    """
    
  return render(request, "auth/signup.html",{"sign_form":sign_form})