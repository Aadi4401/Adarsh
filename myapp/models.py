from django.db import models


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

    specialization=models.CharField(null=True,blank=True,max_length=50)
    doctorname=models.CharField(null=True,blank=True,max_length=50)
    fees=models.IntegerField(null=True,blank=True,default=99)
    date=models.DateField(null=True,blank=True)
    time=models.TimeField(null=True,blank=True)
    patient = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)


class Contact(models.Model):
    name=models.CharField(max_length=35)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=14)
    subject=models.CharField(max_length=50)
    message=models.TextField()
