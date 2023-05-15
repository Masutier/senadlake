from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class LoadFiles(models.Model):
    QUALITY = (
        ('Abiertos', 'Abiertos'),
        ('Privados', 'Privados'),
        ('Clasificados', 'Clasificados'),
    )
    AUTORITY = (
        ('Oficial', 'Oficial'),
        ('Publico', 'Publico'),
    )
    CATEGORY = (
        ('Ciencia', 'Ciencia'),
        ('Comercio', 'Comercio'),
        ('Cultura', 'Cultura'),
        ('Educacion', 'Educacion'),
        ('Medicina', 'Medicina'),
    )
    TERRITORY = (
        ('Nacional', 'Nacional'),
        ('Departamento', 'Departamento'),
        ('Municipio', 'Municipio'),
        ('Zona', 'Zona'),
        ('Barrio', 'Barrio'),
    )
    jsonFile = models.FileField(upload_to='')
    file_ext = models.CharField(max_length=10, null=True)
    file_link = models.CharField(max_length=250, null=True)
    file_name = models.CharField(max_length=100, null=True)
    file_columns = models.JSONField()
    file_numcols = models.IntegerField(null=True)
    file_numrows = models.IntegerField(null=True)
    description = models.CharField(max_length=2500, null=True)
    data_set = models.BooleanField(null=True)
    sheet_set = models.JSONField(null=True)
    license = models.CharField(max_length=25, null=True)
    quality = models.CharField(max_length=80, choices=QUALITY)
    autority = models.CharField(max_length=80, choices=AUTORITY)
    category = models.CharField(max_length=80, choices=CATEGORY)
    territory = models.CharField(max_length=20, choices=TERRITORY)
    downloads = models.IntegerField(null=True,)
    views = models.IntegerField(null=True,)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    clasify_at = models.DateTimeField(null=True)
    published_at = models.DateTimeField(null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.jsonFile)
