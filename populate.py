import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crudProject.settings')

import django
django.setup()

from testapp.models import Employee

from faker import Faker 
from random import *
faker = Faker()


def populate(n):
    for i in range(n):
        fake_emp_no = randint(1, 1600)
        fake_emp_name = faker.name()
        fake_emp_sal =  randint(10000, 25000)
        fake_emp_addr = faker.city()

        emp_record = Employee.objects.get_or_create(
            emp_no = fake_emp_no,
            emp_name = fake_emp_name,
            emp_sal = fake_emp_sal,
            emp_addr = fake_emp_addr
        )

n = int(input("Enter the number of records to be populated : "))
populate(n)

print('='*35)
print(f'{n} no data inserted sucessfully...')
print('='*35)