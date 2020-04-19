from django.shortcuts import render
from django.http import HttpResponse
from .forms import Uploader, Contactussubmit


# Create your views here.

def homeview(request,*args,**kwargs):
   # return HttpResponse("<h2>Welcome to the store</h3>")
    if request.method =='POST':
        form =  Uploader(request.POST)

    form=Uploader()

    return render(request,'home.html',{"form":form})

def aboutview(request,*args,**kwargs):
    #return HttpResponse("<h2>About us</h3>")
    return render(request,'aboutus.html',{})



def contactview(request,*args,**kwargs):
    #return HttpResponse("<h2>Contact us</h3>")

    if request.method =='POST':
        form =  Contactussubmit(request.POST)
        if form.is_valid():
            Name =form.cleaned_data['Name']
            Email=form.cleaned_data['Email']
        print()

    form=Contactussubmit()
    return render(request,'contactus.html',{"form":form})


def serviceview(request,*args,**kwargs):
    #return HttpResponse("<h1> socialpages</h3>")
    return render(request,'services.html',{})





