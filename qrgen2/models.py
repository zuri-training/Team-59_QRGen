from django.db import models
from django.contrib.auth.models import User
from handlescan.models import File

# Create your models here.

ACTION_TYPE = (
    ('web','Website URL'),
    ('tex', 'Text'),
    ('pdf', 'PDF'),
    ('biz', 'Business Card'),
    ('wap', 'Whatsapp'),
    ('img', 'Image'),
    ('eml', 'Email'),
)

class QrType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class QrCode(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey(QrType, on_delete=models.CASCADE)
    img_url = models.CharField(max_length=255)
    action_url = models.URLField(max_length=255)
    action_type = models.CharField(max_length=3, choices=ACTION_TYPE)
    scan_count = models.IntegerField(default=None, null=True, blank=True)
    data_gen = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    file_id = models.ForeignKey(File, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
        
# request.build_absolute_uri(f"/download/{file.id}")