from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Doctors)
class Admindoctor(admin.ModelAdmin):
    list_display =['id','docname','specialization','docfees','docmobile','docemail','docpassword']
