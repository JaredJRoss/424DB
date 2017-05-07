from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import *
from .models import *
from django.views.generic.edit import FormView
from .forms import FileFieldForm
import datetime
from datetime import datetime, timedelta
from django.http import HttpResponseRedirect
import re
from watson import search as watson

def basic_search(request):
    return render(request, 'DAGR/basic_search.html', {})

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
                name = form.cleaned_data.get(Name)
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
