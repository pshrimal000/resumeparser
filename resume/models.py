from django.db import models

# Create your models here.
class ProfileDetail(models.Model):
    file=models.FileField(upload_to='static/')
    number=models.CharField(max_length=225, null=True, blank=True)
    email=models.CharField(max_length=225, null=True, blank=True)
