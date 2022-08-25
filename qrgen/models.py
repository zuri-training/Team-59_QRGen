from django.db import models
from django.contrib.auth.models import User

from cloudinary_storage.storage import RawMediaCloudinaryStorage
from django.core.files.storage import default_storage

from QRGenProject.settings import DEBUG

# Create your models here.

ACTION_TYPE = (
    ('web', 'Website URL'),
    ('tex', 'Text'),
    ('pdf', 'PDF'),
    ('biz', 'Business Card'),
    ('wap', 'Whatsapp'),
    ('img', 'Image'),
    ('eml', 'Email'),
    ('eve', 'Events'),
)


if DEBUG:
    storage = default_storage
else:
    storage = RawMediaCloudinaryStorage()

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='user_files/', storage=storage)

    def __str__(self):
        return self.name


class QrType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class QrCode(models.Model):
    title = models.CharField(max_length=50, null=True, default="Untitled")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey(QrType, on_delete=models.CASCADE)
    is_dynamic = models.BooleanField(default=True, blank=True)
    img = models.ImageField(upload_to='qrcodes/')
    input_url = models.URLField(max_length=255, blank=True, null=True)
    action_url = models.URLField(max_length=255, blank=True, null=True)
    action_type = models.CharField(max_length=3, choices=ACTION_TYPE)
    scan_count = models.IntegerField(default=None, null=True, blank=True)
    date_gen = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    file = models.ForeignKey(
        File, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.title} ({self.date_gen})'

# request.build_absolute_uri(f"/download/{file.id}")
