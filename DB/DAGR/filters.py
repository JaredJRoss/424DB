import django_filters
from .models import *

class DAGRListFilter(django_filters.FilterSet):
    date_between = django_filters.DateTimeFromToRangeFilter(name='CreationTime',label='Date Range')
    Name = django_filters.CharFilter(name = 'Name',lookup_expr = ['contains'])
    Author = django_filters.CharFilter(name = 'Author',lookup_expr = ['contains'])
    Size = django_filters.RangeFilter(name = 'Size')

    class Meta:
        model = DAGR
        fields = '__all__'
        order_by = ['pk']
