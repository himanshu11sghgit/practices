from django.db import models

# Create your models here.

class Image(models.Model):
    img = models.ImageField(upload_to='my_images')
    created_at = models.DateTimeField(auto_now_add=True)