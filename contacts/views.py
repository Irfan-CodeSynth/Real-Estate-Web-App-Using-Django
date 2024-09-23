from django.shortcuts import render , redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
# Create your views here.




def contact(request):
    if request.method == "POST":
        listing_id = request.POST.get('listing_id', '')
        listing = request.POST.get('listing', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        user_id = request.POST.get('user_id', '0')
        realtor_email = request.POST.get('realtor_email', '')

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.filter(listing_id=listing_id, user_id=user_id).exists()
            if has_contacted:
                messages.error(request, "You Have Already Made An Inquiry For This Listing!")
                return redirect('/listings/' + listing_id)

        contact = Contact(
            listing=listing,
            listing_id=listing_id,
            name=name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id,
            realtor_email=realtor_email
        )
        contact.save()
        
        # Send Mail
        send_mail(
            'Property Listing Inquiry',
            'There Has Been An Inquiry For ' + listing + '. Sign Into The Admin Panel For More Info. ',
            'irfankhan.contact786@gmail.com',
            [realtor_email, 'infoirfan.personal@gmail.com'],
            fail_silently=False
        )
        
        messages.success(request, "Your Request Has Been Submitted, A Realtor Will Get Back To You Soon!")
        return redirect('/listings/' + listing_id)
