from django.shortcuts import render
from django.shortcuts import HttpResponse as hr

#for manupulating data from database
from custom_app.models import db,db2

#for all kinds of form
from custom_app.forms import first_form

#class-view in stead of function-view
from django.views.generic import TemplateView,View

#for showing all model objects without query
from django.views.generic import ListView,DetailView





def index(request):
  #data showing from database
  db_list = db2.objects.all()#object of db2 class
  
  if request.method == 'POST':
    dj_form = first_form(request.POST)
  else:
    #showing django forms
    dj_form = first_form()
  
  diction = {"int":4, "veriable":"vAluE","db":db_list, 'form': dj_form}
  return render(request,"custom_app/index.html",context=diction)
  
 
 
  
def blaa(request):
  return render(request,"custom_app/blaa.html",{ "bool":False, "int":345, "str":" hello khadija" })
  
class Blaa(TemplateView):
  template_name = 'custom_app/blaa.html'
  def get_context_data(self,**kwargs):
    context = super().get_context_data(**kwargs)
    context['any_key']='any_value'
    context['any_key2']='any_value2'
    context['bool']=False
    context['int']=34
    context['str']='hello khadija'
    return context
    
    
class Blaa2(View):
  def get(self,request):
    return hr('hello')
    
    
class ModelListView(ListView):
  context_object_name = 'list'
  model = db2
  template_name = 'custom_app/listview.html'
  
  
  
class ModelDetailView(DetailView):
  context_object_name = 'detail_list'
  model = db2
  template_name = 'custom_app/detailview.html'
  """
  for showing all the detail related to this model(as a foreign_key or onetoonefield):
  1. add the argument `related_name='any_name'` to the models.ForeignField() or OneToOneField()
  2. in the tergeted template where the details will be shown,
    {% for x in `model_name`.`related_name`.all %}
      do whatever i want
    {% endfor %}
  """