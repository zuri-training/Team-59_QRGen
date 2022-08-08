from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
ACTION_TYPE = (
    ('web', 'website'),
    ('txt', 'text'),
    ('biz', 'business card'),
    ('pdf', 'pdf'),
    ('wap', 'whatsapp'),
    ('img', 'images'),
    ('eve', 'event'),
    ('eml', 'email')
)


class QrType(models.Model):
    name = models.CharField(max_length=50)


class QrCode(models.Model):
    title = models.CharField(max_length=50, default='untitled')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey(QrType, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='qrcode/')
    # action_url = models.URLField()
    action_type = models.CharField(max_length=3, choices=ACTION_TYPE)
    # scan_count = models.IntegerField()
    date_gen = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    # file = models.OneToOneField()

    def __str__(self):
        return self.title
