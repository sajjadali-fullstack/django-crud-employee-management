from django.db import models

# Create your models / SQL table here.

class Employee(models.Model):
    # emp_no, emp_name, emp_sal, emp_addr
    emp_no = models.IntegerField()
    emp_name = models.CharField()
    emp_sal = models.FloatField()
    emp_addr = models.CharField()