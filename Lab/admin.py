from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Lab_assistant)
class AdminLab_assistant(admin.ModelAdmin):
    list_display = ['id','fname','lname','email','password']