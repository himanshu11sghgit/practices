from django.db import models

# Create your models here.

STATE_CHOICES = (
    ('Delhi', 'Delhi'),
    ('Bihar', 'Bihar'),
    ('Haryana', 'Haryana'),
    ('Goa', 'Goa'),
    ('Kerala', 'Kerala'),
)


class Resume(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField(auto_now_add=False, auto_now=False)
    gender = models.CharField(max_length=255)
    address = models.TextField()
    state = models.CharField(choices=STATE_CHOICES, max_length=255)
    pin = models.IntegerField()
    mobile = models.IntegerField()
    job_city = models.CharField(max_length=255)
    profile_img = models.ImageField(upload_to='my_images', blank=True)
    file = models.FileField(upload_to='my_files', blank=True)
