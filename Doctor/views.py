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
                    return render(request,'header2.html',{'msg':'login successfully'})
                return render(request,'doc_login.html',{'msg':'invalid password'})                        
        except:

             return render(request,'doc_login.html',{'msg':'invalid email'})

    return render(request,'doc_login.html')