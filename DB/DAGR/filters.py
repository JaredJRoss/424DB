import django_filters
from .models import *

class EmployeeListFilter(django_filters.FilterSet):

  class Meta:
    model = Employee
    fields =  '__all__'
    #testing this
    date_between = django_filters.DateFromToRangeFilter(name='DateOfHire',label='Date of Hire (Between)')
    order_by = ['pk']
