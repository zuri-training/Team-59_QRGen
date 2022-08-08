from django.urls import path, include
from rest_framework import routers
from .views import *

app_name = 'api'

# API Home Routes config
router = routers.DefaultRouter()
router.register(r'qrcodes', QrCodeView, 'qrcodes')

urlpatterns = [
    path('', include(router.urls)),
]
