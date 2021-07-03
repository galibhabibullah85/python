from django.db import models as m
from django.db.models import Model as M

# Create your models here.
"""
create database db(
  'id' serial not null primary key,
  'col_name' varcher(20) not null,
  );
"""

#compareable with the sql_code above
class db(M):
  id = m.AutoField(primary_key=True) #using this is q good practice though django automitically manages it
  col_name = m.CharField(max_length=20,default="null")
  """
  some more arguments of __Field():
  null=/bool/
  blank=/bool/ #same as required attribute of html
  """
  
  def __str__(self):
    return self.col_name
    
  """
  for showing a fixed manual name of any database-table:
  class Meta:
    db_table = 'anyname'
  """
  
class db2(M):
  #a primary key will also be created here by django
  #col2 = m.ForeignKey(db, on_delete=m.CASCADE)
  date = m.DateField()
  intgr = m.IntegerField()
  
  choices_like = (
  (1, 'bad'),#same as <option value=1>bad</option>
  (2, 'good'),
  )
  
  intgr2 = m.IntegerField(choices=choices_like,default=5)#the first argument need to be same as the __Field()
  
  """
  choices_like = (
  ('1', 'bad'),
  ('2', 'good'),
  )
  
  intgr2 = m.CharField(choices=choices_like)
  """
  
  def __str__(self):
    return str(self.intgr2)
  
"""
from custom_app import db
print(db.objects.all())#select * from db
print(db.objects.order_by('blaa'))#select * from db order by bla
new_data_insertion = db(col_name='something')
new_data_insertion.save()
"""