from django.contrib import admin
from .models import *


class RaitingAdmin(admin.ModelAdmin):
    list_display = ('message', 'stars', 'date_created')


admin.site.register(Raiting, RaitingAdmin)
