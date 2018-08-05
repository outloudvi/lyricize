from django.db import models

class User(models.Model):
  uid = models.IntegerField(blank=True,default=-1)
  desc = models.TextField(blank=True)
  email = models.TextField(blank=True)
  lastip = models.GenericIPAddressField()
  def __str__(self):
    return  str(self.uid)

class Author(models.Model):
  name = models.TextField(blank=True)
  desc = models.TextField(blank=True)
  def __str__(self):
    return self.name

class Source(models.Model):
  name = models.TextField(blank=True)
  desc = models.TextField(blank=True)
  def __str__(self):
    return self.name

class Category(models.Model):
  name = models.TextField(blank=True)
  desc = models.TextField(blank=True)
  def __str__(self):
    return self.name

class Lyric(models.Model):
  text = models.TextField(blank=True)
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  author = models.ForeignKey(Author,on_delete=models.CASCADE)
  category = models.ManyToManyField(Category)
  source = models.ForeignKey(Source,on_delete=models.CASCADE)
  def __str__(self):
    return self.text