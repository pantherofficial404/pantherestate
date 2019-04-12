from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from contacts.models import Contact
# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,"You Are Logged In")
            return redirect("dashbord")
        else:
            messages.error(request,'Please Enter Valid Credentials')
            return redirect('login')

    else:
        return render(request,'accounts/login.html',{})

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request,"You Are Logged Out")
        return redirect('login')
    else:
        return redirect("dashbord")

def register(request):
    if request.method == "POST":
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        confirmPassword = request.POST['password2']

        if(password==confirmPassword):
            if(User.objects.filter(username=username).exists()):
                messages.error(request,'Username Is Already Exists')
                return redirect('register')
            else:
                if(User.objects.filter(email=email).exists()):
                    messages.error(request,'Email Id Is Exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password,email=email, first_name=firstName, last_name=lastName)
                    user.save()
                    messages.success(request,'You Have Been Registered')
                    return redirect('login')
            
        else:
            messages.error(request,'Please Enter Same Password')
            return redirect('register')
    else:
        return render(request,'accounts/register.html',{})

@login_required()
def dashbord(request):
    contact = Contact.objects.filter(userId=request.user.id)
    context = {
        "contacts" : contact
    }
    return render(request,'accounts/dashbord.html',context)