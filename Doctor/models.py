from django.db import models

# Create your models here.
class Doctors(models.Model):
    docname=models.CharField(max_length=30)
    specialization=models.CharField(max_length=30)
    docfees=models.DecimalField(max_digits=10,decimal_places=2)
    docmobile=models.CharField(max_length=30)
    docemail=models.EmailField(unique=True)
    docpassword=models.CharField(max_length=30)

def __str__(self):
    return self.docemail
