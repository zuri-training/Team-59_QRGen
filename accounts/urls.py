from django.urls import path
from .views import Register, Login, logoutuser
app_name = "accounts"


urlpatterns = [
    path('register/', Register, name="register-page"),
    path('login/', Login, name="login-page"),
    path('logout/', logoutuser, name="logout" )
]