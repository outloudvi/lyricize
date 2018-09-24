from django.db import models
from django.contrib.auth.models import User as sUser

class User(models.Model):
    uid = models.IntegerField(blank=True, default=-1)
    desc = models.TextField(blank=True)
    email = models.TextField(blank=True)
    lastip = models.GenericIPAddressField()

    def __str__(self):
        return str(self.uid)


class Lyric(models.Model):
    text = models.TextField(blank=True)
    user = models.ForeignKey(sUser, on_delete=models.CASCADE)
    author = models.TextField(blank=True)
    category = models.TextField(blank=True)
    source = models.TextField(blank=True)

    def __str__(self):
        return self.text
