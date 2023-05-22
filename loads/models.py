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
        ('Departamental', 'Departamental'),
        ('Municipal', 'Municipal'),
        ('Zonal', 'Zonal'),
        ('Barrio', 'Barrio'),
    )
    jsonFile = models.FileField(upload_to='')

    file_ext = models.CharField(max_length=10, null=True)
    file_link = models.CharField(max_length=500, null=True)
    file_name = models.CharField(max_length=100, null=True)
    file_columns = models.JSONField()
    file_numcols = models.IntegerField(null=True)
    file_numrows = models.IntegerField(null=True)
    description = models.CharField(max_length=2500, null=True)

    data_set = models.BooleanField(null=True)
    sheet_set = models.JSONField(null=True)

    entity = models.CharField(max_length=200, null=True)
    zonas = models.CharField(max_length=25, null=True, default="Raw")

    quality = models.CharField(max_length=20, choices=QUALITY)
    autority = models.CharField(max_length=20, choices=AUTORITY)
    category = models.CharField(max_length=20, choices=CATEGORY)
    territory = models.CharField(max_length=20, choices=TERRITORY)

    downloads = models.IntegerField(null=True,)
    views = models.IntegerField(null=True,)

    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    clasify_at = models.DateTimeField(null=True)
    published_at = models.DateTimeField(null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.jsonFile)


class DataSet(models.Model):
    set_name = models.CharField(max_length=100, null=True)
    data_set = models.BooleanField(null=True)
    sheet_set = models.JSONField(null=True)
    description = models.CharField(max_length=2500, null=True)
    license = models.CharField(max_length=25, null=True)
    entity = models.CharField(max_length=200, null=True)
    zonas = models.CharField(max_length=25, null=True, default="Raw")
    quality = models.CharField(max_length=20)
    autority = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    territory = models.CharField(max_length=20)
    downloads = models.IntegerField(null=True)
    views = models.IntegerField(null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    clasify_at = models.DateTimeField(null=True)
    published_at = models.DateTimeField(null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.set_name)


class SheetFile(models.Model):
    id = models.CharField(max_length=100, primary_key=True, null=False)
    sheet_id = models.IntegerField(null=True)
    sheet_link = models.CharField(max_length=500, null=True)
    sheet_name = models.CharField(max_length=250, null=True)
    main_file = models.CharField(max_length=100, null=True)
    sheet_columns = models.JSONField(null=True)
    sheet_numcols = models.IntegerField(null=True)
    sheet_numrows = models.IntegerField(null=True)
    data_set = models.BooleanField(null=True)
    entity = models.CharField(max_length=200, null=True)
    zonas = models.CharField(max_length=25, null=True, default="Raw")
    downloads = models.IntegerField(null=True,)
    views = models.IntegerField(null=True,)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    clasify_at = models.DateTimeField(null=True)
    published_at = models.DateTimeField(null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.sheet_name)