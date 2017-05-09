import django_filters
from .models import *

class DAGRListFilter(django_filters.FilterSet):

  class Meta:
    model = DAGR
    fields =  '__all__'
    #testing this
    date_between = django_filters.DateFromToRangeFilter(name='CreationTime',label='Date Range')
    order_by = ['pk']
