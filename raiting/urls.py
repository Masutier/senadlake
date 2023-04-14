from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import *


urlpatterns = [
    path('raiting', raiting, name='raiting'),
    path('us', us, name='us'),

    path('testing', testing, name='testing'),

]
