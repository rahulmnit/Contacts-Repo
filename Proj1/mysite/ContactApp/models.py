from django.db import models

# Create your models here.
class Contact(models.Model):
    FullName = models.CharField(max_length=200)
    Phone = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)