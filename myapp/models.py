from django.db import models

# Create your models here.
class atulmodel(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    msg = models.CharField(max_length=255)
