from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import *


urlpatterns = [
    path('loadFile', loadFile, name='loadFile'),
    path('allFiles', allFiles, name='allFiles'),
    path('setFiles', setFiles, name='setFiles'),
    path('xlsAllFiles', xlsAllFiles, name="xlsAllFiles"),

    path('searchFiles/', searchFiles, name='searchFiles'),

    path('setDetail/<pk>', setDetail, name='setDetail'),

    path('csvCall/<pk>', csvCall, name='csvCall'),
    path('xlsxCall/<pk>', xlsxCall, name='xlsxCall'),
    path('jsonCall/<pk>', jsonCall, name='jsonCall'),
    path('pdfCall/<pk>', pdfCall, name='pdfCall'),

]
