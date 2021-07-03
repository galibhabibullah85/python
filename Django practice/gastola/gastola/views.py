from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(requset):
  diction = {
    'title':"GASTOLA | Welcome"
  }
  return render(requset,'index.html',diction)