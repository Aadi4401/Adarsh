
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render


from .models import *
from django.conf import settings
from django.core.mail import send_mail
from random import randrange
from tempfile import tempdir
from Doctor.models import Doctors

import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest

# Create your views here.
# def home(request):
#     return render(request,'index.html') 

def index(request):
    doctor = Doctors.objects.all()
    return render(request,'index.html',{'doctor':doctor})

def getspe(request):
    data = list(Doctors.objects.filter(specialization=request.GET['value']).values())
    return JsonResponse({'data':data})

def Admin(request):
    return render(request,'admin.html')

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
    return render(request,'pchange-password.html',{'uid':uid})


          

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
    uid=User.objects.get(email=request.session['email'])
    doctor = Doctors.objects.all()
    if request.method=='POST':
        Appointment.objects.create(
        specialization=request.POST['specialization'],
        doctorname=request.POST['docname'],
        date=request.POST['date'],
        time=request.POST['time'],
        patient = uid
        
        )
        return render(request,'pay.html',{'uid':uid})
        # return render(request,'appointment.html',{'msg':'Booked!!','uid':uid, 'doctor':doctor,'msg':'Appointment Booked successfully'})
    return render(request,'appointment.html',{'uid':uid,'doctor':doctor})

def contact(request):
    
    if request.method=='POST':
        
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        return render(request,'contact.html',{'msg':'data submitted'})
    return render(request,'contact.html')
    
    #payment integration
razorpay_client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


def pay(request):
    currency = 'INR'
    amount = 20000 # Rs. 200

	# Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
													currency=currency,
													payment_capture='0'))

	# order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'

	# we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
    return render(request, 'pay.html', context=context)

# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request):

	# only accept POST request.
	if request.method == "POST":
		try:
		
			# get the required parameters from post request.
			payment_id = request.POST.get('razorpay_payment_id', '')
			razorpay_order_id = request.POST.get('razorpay_order_id', '')
			signature = request.POST.get('razorpay_signature', '')
			params_dict = {
				'razorpay_order_id': razorpay_order_id,
				'razorpay_payment_id': payment_id,
				'razorpay_signature': signature
			}

			# verify the payment signature.
			result = razorpay_client.utility.verify_payment_signature(
				params_dict)
			# if result is None:
			amount = 20000 # Rs. 200
			try:

				# capture the payemt
				razorpay_client.payment.capture(payment_id, amount)

				# render success page on successful caputre of payment
				return render(request, 'success.html')
			except:

				# if there is an error while capturing payment.
				return render(request, 'fail.html')
			# else:

				# if signature verification fails.
				# return render(request, 'fail.html')
		except:

			# if we don't find the required parameters in POST data
			return HttpResponseBadRequest()
	else:
	# if other than POST request is made.
		return HttpResponseBadRequest()


def cancer(request):
    pass
    return render(request,'cancer.html')
def covid(request):
    pass
    return render(request,'covid.html')
def organ(request):
    pass
    return render(request,'organ.html')

def services(request):
    pass
    return render(request,'services.html')

def about(request):
    pass
    return render(request,'about.html')