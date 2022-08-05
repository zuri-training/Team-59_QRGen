from cmath import log
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from nameparser import HumanName
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def Register(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        password = request.POST.get('pswrd')

        new_user = User.objects.create_user(username = email, email = email, password = password)

        parsed_name = HumanName(fname) 
        new_user.first_name = parsed_name.first
        new_user.last_name = parsed_name.last

        new_user.save()
        return redirect('login-page')

    return render(request, 'accounts/sign up.html', {})

def Login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('pswrd')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('test-page')
        else:
            messages.success(request, 'Email Address and Password  not correct')


    return render(request, 'accounts/sign in.html', {})

#test run delete later

@login_required (login_url='login-page')
def Testdash(request):
    return render(request, 'accounts/dbord.html', {})
