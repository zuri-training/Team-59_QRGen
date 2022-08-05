from django.shortcuts import render

# Create your views here.

def home_page(request):
    # extra context if any
    return render(request, 'home/landing_page.html')
    
def learn_page(request):
    # extra context if any
    return render(request, 'home/learn_page.html')
    
def contact_page(request):
    # extra context if any
    return render(request, 'home/contact_us_page.html')
    
def about_page(request):
    # extra context if any
    return render(request, 'home/about_us_page.html')
    
