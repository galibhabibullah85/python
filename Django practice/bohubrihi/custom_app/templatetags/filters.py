"""
for creating custom template_filters:
1. create new folder 'templatetags' under app_directory
2. under templatetags, create '__init__.py' for making this directory work as a library
3. create a py file with any name under templatetags
"""
from django import template

register = template.Library()

def f_for_type(value):
  return type(value)
  
def add_str(value,arg):
  return f"{value} {arg}"
  
register.filter("type_filter",f_for_type)
register.filter("add_str_filter",add_str)


"""
for accessing custom template_filters:
1. {% load `custom filtered file name with out .py` %}
"""