from django.urls import path
from .views import DynamicCodeScan, download

app_name = 'handlescan'

urlpatterns = [
    path('dynamic/<int:code_id>', DynamicCodeScan.as_view(), name='dynamic'),
    path('download/<int:file_id>', download, name='download'),
]
