from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import *


urlpatterns = [
    path('raiting', raiting, name='raiting'),
    path('testing', testing, name='testing'),

]
