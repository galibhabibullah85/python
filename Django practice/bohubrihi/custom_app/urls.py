from django.urls import path
from . import views

"""
#for better dynamic url-access:
app_name = 'current app name'

#for accessign this dynamic url:
{% url 'current app name:name defined in urls.urlpatterns.path' %}
"""
app_name = "custom_app"

urlpatterns = [
  path("",views.index,name='index'),
  path("list/",views.ModelListView.as_view(),name='list'),
  path("detail/<pk>/",views.ModelDetailView.as_view(),name='detail'),
  #path("blaa/",views.blaa,name='blaa'),
  path("blaa/",views.Blaa.as_view(),name='blaa'),
  ]