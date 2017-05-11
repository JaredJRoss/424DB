from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import InlineField, FormActions, StrictButton


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('Links','Name','Author','Owner','Description')


class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    Author  = forms.CharField()

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class URLForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = '__all__'

class DAGRListFormHelper(FormHelper):
    form_method = 'GET'
    field_template = 'bootstrap3/layout/inline_field.html'
    field_class = 'col-xs-3'
    label_class = 'col-xs-3'
    layout = Layout(
         Fieldset(
                    '<i class="fa fa-search"></i> Search DAGR',
                    InlineField('Name'),
                    InlineField('Author'),
                    'HasKids',
                    'CategoryID',
                    'Size',
                    'date_between',

                ),
                #'resource_first_name',
                #'resource_last_name',
                #'HUBzone',
                #'employment_status',
              Submit('submit', 'Apply Filter'),
    )
