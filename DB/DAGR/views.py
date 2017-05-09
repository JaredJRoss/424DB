from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import *
from .models import *
from django.views.generic.edit import FormView
from .filters import *
from .forms import FileFieldForm
import datetime
from datetime import datetime, timedelta
from django.http import HttpResponseRedirect
import re
from django.views import generic
from watson import search as watson
from .tables import *
from django_tables2 import RequestConfig
from django_tables2 import SingleTableView
from django.views.generic import ListView,TemplateView,UpdateView



def basic_search(request):
    return render(request, 'DAGR/basic_search.html', {})

def tables(request):
    DAGR_table = DAGRTable(DAGR.objects.all())
    RequestConfig(request).configure(DAGR_table)

    return render(request,'DAGR/tables.html',
        {'DAGR':DAGR_table})

class DAGRListView(TemplateView):
    template_name='DAGR/searchable.html'
    def get_queryset(self,**kwargs):
        return DAGR.objects.all()

    def get_context_data(self, **kwargs):
        context = super(DAGRListView, self).get_context_data(**kwargs)
        filter = DAGRListFilter(self.request.GET, queryset=self.get_queryset(**kwargs))
        filter.form.helper = DAGRListFormHelper()
        table = DAGRTable(filter.qs)
        RequestConfig(self.request).configure(table)
        context['filter'] = filter
        context['table'] = table
        return context

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit =False)
            obj.CreationTime = datetime.now()
            obj.Size = form.cleaned_data.get("Links").size
            Type = form.cleaned_data.get('Links').name.split('.')[-1]
            obj.Type = Type
            if not form.cleaned_data.get('Name'):
                name  = form.cleaned_data.get('Links').name.split('/')[-1].split('.')[0]
            else:
                name = form.cleaned_data.get('Name')
            obj.Name = name
            obj.FileName = form.cleaned_data.get('Links').name.split('/')[-1]
            New_DAGR = DAGR(Name = name, Author = form.cleaned_data.get('Author'), \
            CreationTime = datetime.now(), HasKids = False)
            New_DAGR.save()
            obj.Owner = New_DAGR
            obj.save()
        return HttpResponseRedirect('/DAGR/')
    else:
        form = DocumentForm()
    return render(request, 'DAGR/upload.html', {
        'form': form
    })

def find_duplicates(request):
    unique_fields = ['field_1', 'field_n']
    duplicates = (MyModel.objects.values(*unique_fields)
                    .order_by()
                                 .annotate(max_id=models.Max('id'),
                                           count_id=models.Count('id'))
                                 .filter(count_id__gt=1))
    for duplicate in duplicates:
        (MyModel.objects.filter(**{x: duplicate[x] for x in unique_fields})
                        .exclude(id=duplicate['max_id'])
                        .delete())


class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'DAGR/upload.html'  # Replace with your template.
    success_url = 'mult'  # Replace with your URL or reverse().
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            print(form.cleaned_data.get('Author'))
            for f in files:
                New_DAGR = DAGR(Name = f.name, Author = form.cleaned_data.get('Author'), \
                CreationTime = datetime.now(), HasKids = False)
                New_DAGR.save()
                Type = f.name.split('.')[-1]
                New_Doc = Document(Name = f, Author = form.cleaned_data.get('Author'),\
                CreationTime = datetime.now(), Size = f.size, Owner = New_DAGR, \
                Type = Type,Links = f, FileName = f.name)
                New_Doc.save()

            return self.form_valid(form)
        else:
            return self.form_invalid(form)

def add_cat(request):
    form = CategoryForm(request.POST or None);
    name = "Category";
    context = {
        'form' : form,
        'name' : name
    }
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/DAGR/')


    return render(request, 'DAGR/add_new.html', context)

class DAGR_Detailview(generic.DetailView):
    model = DAGR
    template_name='DAGR/detail.html'

class DAGR_Update(UpdateView):
    model = DAGR
    fields = ['Name','Author','Kids']
