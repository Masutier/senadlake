from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from .models import *


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


# class ProfileForm(ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('phone')
#         exclude = ['user']


class LogInForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class UserUpdateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        exclude = ['username', 'password1', 'password2']


class CooperationForm(ModelForm):
    class Meta:
        model = Cooperation
        fields = '__all__'
        exclude = ['join_date']

