from rest_framework.serializers import ModelSerializer
from rest_framework import routers

# from QrGen.models import QrCode
from .models import QrCode

# for the API authentication,
# we shall be using JWT (Json Web Tokens)
# and this will require our User model from 
# the accounts app

# I will be pending the authentication for now

class QrCodeSerializer(ModelSerializer):
    class Meta:
        model = QrCode
        fields = '__all__'
