from django import forms
from .models import *

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('Links','Name','Author')


class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    Author  = forms.CharField()

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
