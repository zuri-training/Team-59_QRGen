
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def LandingPage(request):
    return render (request, 'index.html', {})


def Register(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        password = request.POST.get('pswrd')

        new_user = User.objects.create_user(username = email  ,email = email, password = password)
        new_user.first_name = fname
        
        new_user.save()
        return redirect ('login-page')

    return render (request, 'sign up.html', {} )


def Login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('pswrd')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard-page')
        else:
            return render(request, 'sign in.html', {'error_message': ' Login Failed! Enter your email and password correctly!!', })

    return render(request, 'sign in.html', {})

def logoutuser(request):
    logout(request)
    return redirect('landing-page')

@login_required
def DashBoard(request):
    return render (request, 'dashboard.html', {})


def Learn(request):
    return render (request, 'learn.html', {})

def Features(request):
    return render (request, 'features.html', {})

def About(request):
    return render (request, 'about.html', {})

def Contact(request):
    return render (request, 'contact.html', {})