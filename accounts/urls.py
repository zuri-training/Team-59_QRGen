from django.urls import path
from .views import Register, Login, logoutuser, Testdash
app_name = "accounts"


urlpatterns = [
    path('register/', Register, name="register-page"),
    path('login/', Login, name="login-page"),
    path('logout/', logoutuser, name="logout" ),
    # test run delete later
    path('test/', Testdash, name="test-page")
]