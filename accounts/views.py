from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def Register(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('pswrd')
        uname = request.POST.get('email')
        if User.objects.filter(username = uname).first():
           messages.error(request, 'Email Address Already Exist, Login or Register With Another Email')
        else:
            new_user = User.objects.create_user(username = uname, email = email, password = password)

            new_user.first_name = fname
            new_user.last_name = lname

            new_user.save()
            return redirect('accounts:login-page')

    return render(request, 'accounts/register.html', {})

def Login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('pswrd')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect()
        else:
            messages.error(request, 'Email Address and Password do not exist')


    return render(request, 'accounts/login.html', {})

def logoutuser(request):
    logout(request)
    return redirect('accounts:login-page')

