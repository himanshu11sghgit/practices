from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Github(models.Model):
    github_user = models.CharField(max_length=255)
    image_link = models.CharField(max_length=255)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)


    def __str__(self):
        return self.github_user
