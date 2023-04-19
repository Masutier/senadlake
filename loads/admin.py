from django.contrib import admin
from .models import *


class loadFilesAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'file_ext', 'autority', 'category', 'territory', 'uploaded_at')


admin.site.register(LoadFiles, loadFilesAdmin)
