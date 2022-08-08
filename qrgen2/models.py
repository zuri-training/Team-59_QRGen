from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class QrType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class QrCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey(QrType, on_delete=models.CASCADE)
    img_url = models.CharField(max_length=255)
    action_url = models.URLField(max_length=255)


    # request.build_absolute_uri(f"/download/{file.id}")