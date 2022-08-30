from django.db import models

# Create your models here.

STATE_CHOICES = (
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Delhi', 'Delhi'),
    ('Goa', 'Goa'),
    ('Haryana', 'Haryana'),
)


class Resume(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=255)
    locality = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    pin = models.PositiveIntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=255)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=255  )
    image = models.ImageField(upload_to='my_images', blank=True)
    file = models.FileField(upload_to='my_files', blank=True)
