
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import *
from django.conf import settings
from django.core.mail import send_mail
from random import randrange
from tempfile import tempdir
from Doctor.models import Doctors

# Create your views here.
def home(request):
    return render(request,'index.html')

def index(request):
    return render(request,'index.html')
    
def Admin(request):
    return render(request,'admin.html')

def otp(request):
    return render(request,'otp.html')
def dashboard(request):
    uid = User.objects.get(email=request.session['email'])
    return render(request,'header.html',{'uid':uid})

def register(request):
    if request.method == "POST":
        try:          
            User.objects.get(email=request.POST['email']) 
            msg = 'Email is already register'
            return render(request,'patient.html',{'msg':msg})
        except:
            if request.POST['password']==request.POST['cpassword']:
                global temp
                temp={
                'uname':request.POST['uname'],
                'email':request.POST['email'],
                'password':request.POST['password'],

                }
                otp=randrange(1111,9999)
                subject='Welcome to GFG world'
                message=f'Welcome to Life Care {otp}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST['email'], ]
                send_mail( subject, message, email_from, recipient_list )
                return render (request,'otp.html',{'otp':otp})
            else:
                return render(request,'patient.html',{'msg':'Both passwords are not same'})
    return render(request,'patient.html')
def otp(request):
    if request.method=="POST":
        if request.POST['otp']==request.POST['uotp']:
            global temp
            User.objects.create(
            uname=temp['uname'],
            email=temp['email'],
            password=temp['password'],
        )
            return render(request,'patient.html',{'msg':'Account Created '})
        return render(request,'otp.html',{'msg':'Invalid OTP','otp':request.POST['otp']})
    return render(request,'patient.html')

#login
def login(request):
    try:
        uid=User.objects.get(email=request.session['email'])
        return render(request,'pdash.html',{'uid':uid})
    except:
        if request.method=="POST":
            try:
                uid=User.objects.get(email=request.POST['email'])
                if request.POST['password']==uid.password:
                    request.session['email'] = request.POST['email']
                    return render(request,'pdash.html',{'uid':uid})
                return render(request,' patient.html',{'msg':'invalid password','uid':uid})
            except:
                return render(request,'patient.html',{'msg':'email not register','uid':uid})
        return render(request,'patient.html')

   
       

#patient dashboard
def pdash(request):
    if request.method=="POST":
        return render(request,'pdash.html')
    return render(request,'patient.html')

def logout(request):
    del request.session['email']
    return render(request,'patient.html')

def pchange_password(request):
    uid=User.objects.get(email=request.session['email'])
    if request.method=='POST':
        if request.POST['opassword']==uid.password:
            if request.POST['npassword']==request.POST['rpassword']:
                uid.password=request.POST['npassword']
                uid.save()
                return render(request,'pchange-password.html',{'msg':'Password Changed Successfully','uid':uid})
            return render(request,'pchange-password.html',{'msg':'New passwords are not same','uid':uid})
        return render(request,'pchange-password.html',{'msg':'Old password is incorrect','uid':uid})
    return render(request,'pchange-password.html')


          

def pforgot_password(request):

    if request.method=='POST':

        try:

            uid=User.objects.get(email=request.POST['email'])
            if request.POST['email']==uid.email:
                fpass=uid.password
                subject='your password for login'
                message=f'Welcome to Life Care your password for login is: {fpass}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST['email'], ]
                send_mail( subject, message, email_from, recipient_list )
                return render(request,'pforgot-password.html',{'msg':'password sent successfully'})        
        except:
            return render(request,'pforgot-password.html',{'msg':'invalid email'})
    return render(request,'pforgot-password.html')                     


def p_profile(request):
    uid=User.objects.get(email=request.session['email'])
    if request.method =='POST':
        uid.uname=request.POST['uname']
        uid.email=request.POST['email']
        uid.fname=request.POST['fname']
        uid.lname=request.POST['lname']
        uid.mobile=request.POST['mobile']
        uid.age=request.POST['age']
        uid.address=request.POST['address']        
        if 'pic' in request.FILES:
            uid.pic=request.FILES['pic']
        uid.save()
        return render(request,'p_profile.html',{'uid':uid,'msg':'Profile has been updated successfully'})
    return render(request,'p_profile.html',{'uid':uid})

def my_profile(request):
    uid=User.objects.get(email=request.session['email'])
    return render(request,{'uid'.uid})

def appointment(request):
    try:
        uid=User.objects.get(email=request.session['email'])
        if request.method == "GET":
            docs=Doctors.objects.all
            specs = Doctors.objects.filter(docs.specialization)
            return render(request,'appointment.html',{'uid':uid,'docs':docs,})
            
    except:
        return render(request,'appointment.html')
   

    