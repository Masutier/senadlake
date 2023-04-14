from django import forms
from django.db import models
from django.forms import ModelForm
from .models import LoadFiles


class loadFileForm(ModelForm):

    class Meta:
        model = LoadFiles
        fields = ('file', 'description', 'autority', 'category', 'territory')
        exclude = ['file', 'file_ext', 'file_link', 'downloads', 'views', 'uploaded_at', 'clasify_at', 'published_at', 'updated']
