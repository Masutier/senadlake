from django.db import models


class Raiting(models.Model):
    message = models.TextField(max_length=3000, blank=True, null=True)
    stars = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.message
