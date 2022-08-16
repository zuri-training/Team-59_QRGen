from django.shortcuts import render

# Create your views here.

def home_page(request):
    # extra context if any
    return render(request, 'home/landing_page.html', {'title': 'Home'})
    
def learn_page(request):
    # extra context if any
    return render(request, 'home/learn_page.html', {'title': 'Learn'})
    
def contact_page(request):
    # extra context if any
    return render(request, 'home/contact_us_page.html', {'title': 'Contact Us'})
    
def about_page(request):
    # extra context if any
    return render(request, 'home/about_us_page.html', {'title': 'About Us'})

def documentation(request):
    # extra context if any
    return render(request, 'home/documentation_page.html', {'title': 'APU Documentation'})

def not_found(request, exception):
    return render(request, '404.html', {'title': 'Page not found'})
