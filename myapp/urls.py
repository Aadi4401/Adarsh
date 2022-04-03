from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    
    # path('',views.home,name="home"), 
    path('',views.index,name="index"),
    

     


    path('Admin/',views.Admin,name="Admin"),
    path('register/',views.register,name="register"),
    path('otp/',views.otp,name="otp"),
    path('getspe/',views.getspe,name="getspe"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('pdash/',views.pdash,name="pdash"),
    path('pchange_password/',views.pchange_password,name="pchange_password"),
    path('pforgot_password/',views.pforgot_password,name="pforgot_password"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('p_profile/',views.p_profile,name="p_profile"),
    path('my_profile/',views.my_profile,name="my_profile"),
    path('appointment/',views.appointment,name="appointment"),
    path('contact/',views.contact,name="contact"),
     
]
