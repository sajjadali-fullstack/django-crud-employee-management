from django.shortcuts import render, redirect
from testapp.models import Employee
# Create your views / business logic here.

def retrive_view(request):
    emp_list = Employee.objects.all()
    return render(request, 'testapp/index.html', {'emp_list':emp_list})



from testapp.forms import EmployeeForm

def insert_view(request):
    form = EmployeeForm()
    if request.metho == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'testapp/insert.html', {'form':form})