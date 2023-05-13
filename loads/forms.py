from django import forms
from django.db import models
from django.forms import ModelForm
from .models import LoadFiles


class loadFileForm(ModelForm):

    class Meta:
        model = LoadFiles
        fields = ('jsonFile', 'description', 'quality', 'autority', 'category', 'territory')
        exclude = ['jsonFile', 'file_ext', 'file_link', 'file_name', 'file_numcols', 'file_numrows', 'file_columns', 'downloads', 'data_set', 'views', 'uploaded_at', 'clasify_at', 'published_at', 'updated']
