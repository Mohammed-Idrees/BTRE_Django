from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

# Create your views here.

def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        realtor_email = request.POST['realtor_email']
        user_id = request.POST['user_id']

        if request.user.is_authenticated:
            user_id =request.user.id
            has_contacted = Contact.objects.all().filter(user_id=user_id,listing_id=listing_id)

            if has_contacted:
                messages.error(request,'you have already made and inquiry for this listing')
                return redirect('/listings/'+listing_id)


        contact = Contact(listing_id=listing_id,name=name,listing=listing,
                          email=email,phone=phone,message=message,user_id=user_id)
        contact.save()

        send_mail(
            'Property Listing Inquiry',
            'There has been and inquiry for '+ listing + '. Sign into the admin panel for more info',
            'mohmad.edris@terralogic.com',
            [realtor_email,'itsmohmadedris@gmail.com'],
            fail_silently=False
        )

        messages.success(request,'Your request has been submitted, a realtor will get back to you soon')
        return redirect('/listings/'+listing_id)