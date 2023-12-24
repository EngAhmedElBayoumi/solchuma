from django.shortcuts import render
from .models import Country_code, Message_type, contact, contact_message
#import messages
from django.contrib import messages
# Create your views here.

def Contact(request):
    #get contact information
    contact_info = contact.objects.all()
    #get country code
    country_code = Country_code.objects.all()
    #get message type
    message_type = Message_type.objects.all()
    context={
        'contact_info':contact_info,
        'country_code':country_code,
        'message_type':message_type,
    }
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        country_code = request.POST['country_code']
        message_type = request.POST['message_type']
        subject = request.POST['subject']
        message = request.POST['message']
        #save contact message
        contact_message.objects.create(
            name=name,
            email=email,
            phone=phone,
            country_code_id=country_code,
            message_type_id=message_type,
            subject=subject,
            message=message
        )
        #send message
        messages.success(request, 'Your Message Has Been Sent Successfully')
    return render(request, 'contact.html', context)

def contact_ar(request):
    #get contact information
    contact_info = contact.objects.all()
    #get country code
    country_code = Country_code.objects.all()
    #get message type
    message_type = Message_type.objects.all()
    context={
        'contact_info':contact_info,
        'country_code':country_code,
        'message_type':message_type,
    }   
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        country_code = request.POST['country_code']
        message_type = request.POST['message_type']
        subject = request.POST['subject']
        message = request.POST['message']
        #save contact message
        contact_message.objects.create(
            name=name,
            email=email,
            phone=phone,
            country_code_id=country_code,
            message_type_id=message_type,
            subject=subject,
            message=message
        )
        #send message
        messages.success(request, 'تم إرسال رسالتك بنجاح')
    return render(request, 'ar/contact.html', context)