from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

from .models import Booking, Contact


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def packages(request):
    return render(request, 'packages.html')

def online_booking(request):
    return render(request, 'online_booking.html')

def contact(request):
    return render(request, 'contact.html')

def store_booking(request):
    if request.method == 'POST':
        booking = Booking()
        name = request.POST['name']
        email = request.POST['email']
        description = request.POST['description']

        
        booking.name = name
        booking.email = email
        booking.description = description

        if(name and email and description):
            booking.save()
            messages.info(request, "Thank You, your information is sent to the admin, we'll let you inform soon")
            return render(request, 'online_booking.html')
        #Booking.objects.create(name, email, description)
        return render(request, 'online_booking.html')
    else:
        return render(request, 'online_booking.html')


def store_contact(request):
    if request.method == 'POST':
        email = request.POST['email']
        phone = request.POST['phone']
        details = request.POST['details']
        
        contact = Contact()
        contact.email = email
        contact.phone = phone
        contact.details = details

        if(email and phone and details):
            contact.save()
            messages.info(request, "Thank You, your information is sent to the admin, we'll let you inform soon")
            return render(request, 'contact.html')
        else:
            return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')


