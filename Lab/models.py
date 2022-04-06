from django.db import models

# Create your models here.

class Lab_asistant(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=30)
    lab_pic=models.FileField(upload_to='profile',default='lab.png')

def __str__(self):
    return self.email