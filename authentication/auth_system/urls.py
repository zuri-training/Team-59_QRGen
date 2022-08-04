from django.urls import path
from .views import LandingPage, Register, Login, logoutuser , DashBoard, Features, About, Contact, Learn

urlpatterns = [
    path('', LandingPage, name="landing-page"),
    path('register/', Register, name="register-page"),
    path('login/', Login, name="login-page"),
    path('logout/', logoutuser, name="logout"),
    path('dashboard/', DashBoard, name="dashboard-page"),
    path('features/', Features, name="feature-page"),
    path('about/', About, name="about-page"),
    path('learn/', Learn, name="learn-page"),
    path('contact/', Contact, name="contact-page")
]