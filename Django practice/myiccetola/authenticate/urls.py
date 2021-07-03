from django.urls import path
from . import views

app_name = "authenticate"

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.sign_up, name='signup'),
    #path('signup/<`data_type(for example: int,str,bool)`:`get_veriable_name`>', views.sign_up, name='signup'),
]