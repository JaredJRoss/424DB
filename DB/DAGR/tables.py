import django_tables2 as tables
from .models import *
from django_tables2.utils import A  # alias for Accessor

class DAGRTable(tables.Table):
    id = tables.LinkColumn('dagr_detail',args=[A('pk')])
    class Meta:
        model = DAGR
        attrs = {'class': 'paleblue'}
