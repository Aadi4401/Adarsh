from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(User)

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ['uname','password','id','email','pic','fname','lname','mobile','age','address']
   
@admin.register(Appointment)
class AdminAppointment(admin.ModelAdmin):
    list_display = ['id','specialization','doctorname','fees','date','time']

@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ['id','name','email','phone','subject','message']
 
