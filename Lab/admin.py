from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Lab_asistant)
class AdminLab_assistant(admin.ModelAdmin):
    list_display = ['id','fname','lname','email','password','lab_pic']
 