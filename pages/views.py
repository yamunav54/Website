from django.shortcuts import render
from django.http import HttpResponse
from .forms import Uploader, Contactussubmit
from django.core.mail import send_mail
from django.core import mail
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.conf import settings



# Create your views here.
def homeview(request):
   # return HttpResponse("<h2>Welcome to the store</h3>")
    if request.method =='POST':
        form =  Uploader(request.POST)
        if form.is_valid():
            Firstname=request.POST.get('Firstname','')
            Lastname=request.POST.get('Lastname','')
            Phoneno=request.POST.get('Phoneno','')
            Email=request.POST.get('Email','')
            Qualification=request.POST.get('Qualification','')
            Cv=request.POST.get('Cv','')
            mail.send_mail(Firstname,Lastname,Phoneno,Email,Qualification,Cv,['***@gmail.com'],fail_silently=False)
            messages.info(request,'Message Sent Successfully')

    form=Uploader()
    return render(request,'home.html',{"form":form})

def aboutview(request,*args,**kwargs):
    #return HttpResponse("<h2>About us</h3>")
    return render(request,'aboutus.html',{})



def contactview(request):
    #return HttpResponse("<h2>Contact us</h3>")

    if request.method =='POST':
        form =  Contactussubmit(request.POST)
        if form.is_valid():
            Name=request.POST.get('name','')
            Phone=request.POST.get('Phone','')
            Message=request.POST.get('Message','')
            mail.send_mail(Name,Phone,Message,['anumayconsultancy@gmail.com'],fail_silently=False)
            messages.info(request,'Message Sent Successfully')
    form=Contactussubmit()
    return render(request,'contactus.html',{"form":form})


def serviceview(request,*args,**kwargs):
    #return HttpResponse("<h1> socialpages</h3>")
    return render(request,'services.html',{})





