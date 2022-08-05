from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='user_files/')

    def __str__(self):
        return self.name


class QrCode():
    '''
        JUST A DEMO
        Real model in 'qrgen' app
    '''
    pass