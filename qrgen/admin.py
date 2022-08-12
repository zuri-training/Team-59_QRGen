from django.contrib import admin
from .models import File, QrCode, QrType
# Register your models here.

admin.site.register(File)
admin.site.register(QrCode)
admin.site.register(QrType)

