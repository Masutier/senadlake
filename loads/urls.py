from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import *


urlpatterns = [
    path('loadFile', loadFile, name='loadFile'),
    path('allFiles', allFiles, name='allFiles'),
    path('setFiles', setFiles, name='setFiles'),
    path('searchFiles/', searchFiles, name='searchFiles'),

]
