from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    
    path('', views.doc_login, name="doc_login"),
    path('view_appointment/', views.view_appointment, name="view_appointment"),
    path('doc_logout/', views.doc_logout, name="doc_logout"),

   
]