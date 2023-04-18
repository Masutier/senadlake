from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.user)


class Cooperation(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, null=False, blank=False)
    jobDone = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    photo = models.ImageField(default='media/img/default.jpg', upload_to='media/img')
    join_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.user)
