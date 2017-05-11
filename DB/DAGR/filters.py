import django_filters
from .models import *

def reach_help(pk,arr):
    print(arr)
    Cat = Category.objects.get(ParentCategory=pk)
    arr.append(Cat)
    if Cat.ParentCategory:
        reach_help(Cat.pk,arr)
    return arr

class DAGRListFilter(django_filters.FilterSet):
    all_cat = DAGR.objects.prefetch_related('CategoryID')
    date_between = django_filters.DateTimeFromToRangeFilter(name='CreationTime',label='Date Range')
    Name = django_filters.CharFilter(name = 'Name',lookup_expr = ['contains'])
    Author = django_filters.CharFilter(name = 'Author',lookup_expr = ['contains'])
    Size = django_filters.RangeFilter(name = 'Size')
    CategoryID = django_filters.ModelChoiceFilter(queryset=Category.objects.all(),method = 'custom_filter')
    class Meta:
        model = DAGR
        fields = '__all__'
        order_by = ['pk']



    def custom_filter(self, queryset, name, value):
        arr = []
        print('Name')
        print(name)
        print('value')
        print(value.pk)
        print(reach_help(value.pk,arr))
        for i in arr:
            return queryset.filter(**{
                name:i,
            })
