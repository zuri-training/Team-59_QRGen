from django.db import models
from django.contrib.auth.models import User

# Create your models here.

'''
QR_TYPE = (
    ('DYN', 'Dynamic'),
    ('STA', 'Static'),
)

# class QrType(models.Model):
#     name = models.CharField(max_length=10)
#     def __str__(self):
#         return self.name


class QrCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=3, choices=QR_TYPE)
    # type = models.ForeignKey(QrType, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='qrcodes/')
    action_url = models.URLField(max_length=255)

    def __str__(self):
        return self.user.username

'''
    
class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='user_files/')

    def __str__(self):
        return self.name

