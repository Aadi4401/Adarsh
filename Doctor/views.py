import email
from django.shortcuts import render

from Doctor.models import Doctors


# Create your views here.
def doc_login(request):

    if request.method=="POST":
        try:
            doc=Doctors.objects.get(docemail=request.POST['docemail'])
            if request.POST['docemail']==doc.docemail:
                if request.POST['docpassword']==doc.docpassword:
                    return render(request,'header2.html',{'msg':'login successfully','doc':doc})
                return render(request,'doc_login.html',{'msg':'invalid password','doc':doc})                        
        except:
             return render(request,'doc_login.html',{'msg':'invalid email','doc':doc})
    return render(request,'doc_login.html')

def doc_logout(request):
    del request.session['docemail']
    return render(request,'doc_login.html')

def view_appointment(request):
    if request.method=='GET':

        return render(request,'view_appointment.html')
