from contextlib import nullcontext
from re import M
from django.db import models
from django.forms import CharField, DateField, IntegerField, TimeField





# Create your models here.

class User(models.Model):

    uname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    pic = models.FileField(upload_to='profile',default='avatar.png')
    fname=models.CharField(max_length=30,null=True)
    lname=models.CharField(max_length=30,null=True)
    mobile=models.CharField(max_length=15,null=True)
    age=models.CharField(max_length=30,null=True)
    address=models.TextField(null=True,blank=True)

    
def __str__(self):
    return self.email

class Appointment(models.Model):
    
    specialization=CharField(max_length=30)
    doctorname=CharField(max_length=35)
    fees=IntegerField(min_value=500)
    date=DateField(required=True)
    time=TimeField(required=True)



