from django.contrib import admin
from testapp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['emp_no', 'emp_name', 'emp_sal', 'emp_addr']
    search_fields = ['emp_name']
    list_filter = ['emp_sal']
    ordering = ['emp_no']
    readonly_fields = ['emp_sal']
  


# Register your models here.
admin.site.register(Employee, EmployeeAdmin)