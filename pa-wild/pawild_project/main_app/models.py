from django.db import models
from django import forms


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254,unique=True)
    text = models.TextField(max_length=500, blank=True)
