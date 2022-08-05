from django.shortcuts import render, redirect
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

        new_user = User.objects.create_user(username = email, email = email, password = password)

        new_user.first_name = fname
        new_user.last_name = lname

        new_user.save()
        return redirect('accounts:login-page')

    return render(request, 'accounts/sign up.html', {})

def Login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('pswrd')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:test-page')
        else:
            messages.success(request, 'Email Address and Password do not exist')


    return render(request, 'accounts/sign in.html', {})

def logoutuser(request):
    logout(request)
    return redirect('accounts:login-page')

#test run delete when dashboard is ready
@login_required (login_url='accounts:login-page')
def Testdash(request):
    return render(request, 'accounts/dbord.html', {})
