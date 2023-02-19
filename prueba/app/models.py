from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(blank=False, max_length=100)
    email = models.EmailField(max_length=100)
    last_name = models.CharField(blank=False, max_length=100)