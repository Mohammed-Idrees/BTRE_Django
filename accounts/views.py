from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    if request.method == 'POST':
        # messages.error(request,'Testing Error Message')
        # return redirect('register')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #Check if passwords match
        if password==password2:
            #Check Username

            if User.objects.filter(username=username).exists():
                messages.error(request, 'This User name is already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'This email is already taken')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username,email=email,
                            first_name=first_name, last_name=last_name,
                            password=password)
                    #Login after Register
                    # auth.login(request,user)
                    # messages.success(request,'You are now logged in')
                    # return redirect('index')

                    user.save()
                    messages.success(request,'You are now registered and can login')
                    return redirect('login')

        else:
            messages.error(request,'Passwords do not match')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')

def dashboard(request):
    return render(request,'accounts/dashboard.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are now logged out')
        return redirect('index')