from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from contacts.models import Contact
from django.core.mail import send_mail
# Create your views here.

@login_required
def contact(request):
    if request.method == "POST":
        listing = request.POST['listing']
        listingId = request.POST['listingId']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        inquiry = Contact(listing=listing,listingId=listingId,name=name,email=email,phone=phone,message=message,userId=request.user.id)
        inquiry.save()
        send_mail(
            "Panther Estate - Inquiry",
            "Thank You For Take Interest In Our Webapp We Will Shortly Bring Some New Features Into It",
            'pantherofficial404@gmail.com',
            [email],
            fail_silently=False
        )
        messages.success(request,"Your Query Has Been Successfully Placed")
        return redirect("/listings/"+listingId)
    return redirect("home")