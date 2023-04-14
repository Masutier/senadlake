from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return str(self.user)
