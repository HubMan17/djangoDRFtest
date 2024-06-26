from django.db import models

# Create your models here.

class Author(models.Model):
  name = models.CharField(max_length=100)
  age = models.IntegerField()

class Book(models.Model):
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  price = models.IntegerField()
  date = models.DateField(auto_now=True)
