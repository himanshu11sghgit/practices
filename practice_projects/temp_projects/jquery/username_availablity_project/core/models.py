from django.db import models

# Create your models here.



class Username(models.Model):
    name = models.CharField(max_length=255)
    