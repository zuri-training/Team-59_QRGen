from django.urls import path
from .views import Register, Login, Testdash

urlpatterns = [
    path('register/', Register, name="register-page"),
    path('login/', Login, name="login-page"),
    # test run delete later
    path('test/', Testdash, name="test-page")
]