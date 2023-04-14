from django.db import models
from django import forms
from django.forms import ModelForm, TextInput, EmailInput
from captcha.fields import ReCaptchaField
from .models import *


class RaitingForm(ModelForm):

    class Meta:
        model = Raiting
        fields = ['message', 'stars']
        exclude = ['date_created']

