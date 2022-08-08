from django.shortcuts import render
from rest_framework import viewsets
from .serializers import QrCodeSerializer

# from QrGen.models import QrCode
from .models import QrCode

# for JWT auth
from rest_framework.permissions import IsAuthenticated


class QrCodeView(viewsets.ModelViewSet):
    serializer_class = QrCodeSerializer
    queryset = QrCode.objects.all()
    # permission_classes = (IsAuthenticated,)
