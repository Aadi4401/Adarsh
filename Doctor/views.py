import email
from django.shortcuts import render

from Doctor.models import Doctors
from myapp.models import Appointment


# Create your views here.
def doc_login(request):

    if request.method=="POST":
        try:
            doc=Doctors.objects.get(docemail=request.POST['docemail'])
            

            if request.POST['docemail']==doc.docemail:
                if request.POST['docpassword']==doc.docpassword:
                    request.session['docemail'] = request.POST['docemail']
                    return render(request,'header2.html',{'msg':'login successfully','doc':doc})
                return render(request,'doc_login.html',{'msg':'invalid password','doc':doc})                        
        except:
             return render(request,'doc_login.html',{'msg':'invalid email','doc':doc})
    return render(request,'doc_login.html')

def doc_logout(request):
    del request.session['docemail']
    return render(request,'doc_login.html')

def view_appointment(request):
    doctor=Doctors.objects.get(docemail=request.session['docemail'])
    appointments =Appointment.objects.filter(doctorname=doctor.docname)
    
    print(appointments)
    return render(request,'view_appointment.html',{'appointments':appointments,'doctor':doctor})
