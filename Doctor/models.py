from django.db import models
from django.forms import FileField

# Create your models here.
class Doctors(models.Model):
    docname=models.CharField(max_length=30)
    specialization=models.CharField(max_length=30)
    docfees=models.DecimalField(max_digits=10,decimal_places=2)
    docmobile=models.CharField(max_length=30)
    docemail=models.EmailField(unique=True)
    docpassword=models.CharField(max_length=30)
    doc_pic=models.FileField(upload_to='profile',default='doc.png')

def __str__(self):
    return self.docemail
