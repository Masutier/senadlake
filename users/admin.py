from django.contrib import admin
from .models import *


class CooperationAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'jobDone')


admin.site.register(Cooperation, CooperationAdmin)
