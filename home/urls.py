from django.urls import path
from .views import home_page, about_page, learn_page, contact_page, documentation

app_name = 'home'

urlpatterns = [
    path('', home_page, name='home-page'),
    path('about-us/', about_page, name='about-page'),
    path('learn/', learn_page, name='learn-page'),
    path('contact-us/', contact_page, name='contact-page'),
    path('documentation/',documentation, name='documentation-page')
]
