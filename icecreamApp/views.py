from ast import If
from unicodedata import name
from django.shortcuts import render, HttpResponse
from datetime import date, datetime
from .models import contact
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def flavour(request):
    return render(request,'chocolate.html')

def dryfruit(request):
    return render(request,'dryfruit.html')

def fruit(request):
    return render(request,'fruit.html')

def indiantrde(request):
    return render(request,'indiantrde.html')

def inter(request):
    return render(request,'inter.html')

def contact1(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email') 
        Phone = request.POST.get('Phone')
        desc = request.POST.get('desc')
        Contactsave = contact(name=name, email=email, Phone=Phone, desc=desc, date=datetime.today())
        Contactsave.save()
        messages.success(request, 'Your message has been sent!')

    return render(request,'contact.html') 

